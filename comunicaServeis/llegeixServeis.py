#!/usr/bin/python
# coding=UTF8

#Importem les llibreries necessàries
import os, sys, datetime, requests, shutil

#Llegim línia a línia el fitxer origen de les dades
def llegeixFitxer():

    #Obrim per lectura el fitxer origen de les dades
    fitxer ='serveis.csv'

    with open(fitxer,'r') as serveis:
        #El llegim línia a línia
        for servei in serveis.readlines()[1:]:
            servei = servei.rstrip()
            #Separem els valors llegit quan trobem un tabulador
            #i n'assignem els valors a les variables
            cond, chatid, missatge, document = servei.split('\t')
            #Enviem les dades llegides
            enviaComunicacio(chatid,missatge,document)
        #Cridem la funció que mou el fitxer de serveis al directori d'històrics
        canviaFitxer(fitxer)

#Enviem als destinataris les dades llegides del fitxer
def enviaComunicacio(chatid, missatge, document):

    #Definim els paràmetres necessaris per l'API de Telegram
    url = "https://api.telegram.org/bot"
    token = "BOT_TOKEN"
    accioM = "/sendMessage"
    accioD = "/sendDocument"

    #Construïm la url del POST pel missatge
    peticio1 = requests.post(url+token+accioM, params={'chat_id': chatid, 'text': missatge})

    if document not in ['x','X']: #Si la columna del fitxer té una "x", no intentem enviar-lo
        with open(document,'rb') as fitxerenviat:
            #Construïm la url del POST pel fitxer
            peticio2 = requests.post(url+token+accioD, files={'document': fitxerenviat}, data={'chat_id': chatid})

def canviaFitxer(fitxer):

    desti = 'historic_serveis/'
    if fitxer == 'serveis.csv':
        shutil.move(fitxer, desti + fitxer + "." + ('{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())))

def main():
    llegeixFitxer()

main()
#!/usr/bin/python
# coding=UTF8

#Importem les llibreries necessàries
import os, sys, datetime, shutil

ORACLE_HOME=/oracle/PRD/102_64; export ORACLE_HOME
PATH=$ORACLE_HOME/bin:$PATH; export PATH
ORACLE_SID=PRD; export ORACLE_SID

export_dir = "/oracle/PRD/export_trip/"
export_file = "exportacio.dmp"
export_log = "exportacio.log"
user = john
host = doe
ouser = usuari
opasswd = administrador

def dump():
    os.system("expdp " + ouser + "/" + opasswd + " tables=SAPSR3.IBINVALUES,SAPSR3.AFVC,SAPSR3.AUFK,SAPSR3.AFKO,SAPSR3.KNA1,SAPSR3.VBAP,SAPSR3.IBIN,SAPSR3.VBEP,SAPSR3.VBAK,SAPSR3.IBSYMBOL,SAPSR3.MARA,SAPSR3.KNA1,SAPSR3.CRHD,SAPSR3.CRTX,SAPSR3.FLEET,SAPSR3.TC23,SAPSR3.TC23T,SAPSR3.TC30T,SAPSR3.ZPPAUTOCOND,SAPSR3.T023,SAPSR3.T023T,SAPSR3.CABN directory=" + export_dir + " dumpfile=" + export_file + " logfile=" + export_log + " QUERY='"WHERE MANDT=900"'")

def compress():
    os.system("gzip -f " + export_dir + export_file)

def transfer_datafile():
    os.system("rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"" + export_dir + "/" + export_file + ".gz " + user + "@" + host + ":" + export_dir)
    
def transfer_logfile():
    os.system("rsync -avz -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"" + export_dir + "/" + export_log + ".gz " + user + "@" + host + ":" + export_dir)

"""def canviaFitxer(fitxer):
    desti = 'incidencies_dump/'
    if fitxer == 'serveis.csv':
        shutil.move(fitxer, desti + fitxer + "." + ('{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())))"""

if os.path.isfile(export_file):
    mou-lo al directori d'incidències i envia una notificació per algun mitjà
    dump()
    else:
        dump()
        


def main():
    llegeixFitxer()

main()

# Uses python3
import sys

def demanadades():
    nombre, pesadmes = map(int, input().split())
    print(nombre, pesadmes)
    llistavalors = [None] * nombre
    llistapesos = [None] * nombre
    for item in range(0, nombre):
        llistavalors[item], llistapesos[item] = map(int, input().split())
    return nombre, pesadmes, llistavalors, llistapesos

def agafa_valoroptim(nombre, pesadmes, llistavalors, llistapesos):
    valortotal = 0.
    llistarati = [None] * nombre
    for i in range(0, nombre):
        llistarati[i] = int(llistavalors[i]) / int(llistapesos[i])
        print(llistarati[i])
    #print(llistarati, llistavalors, llistapesos,len(llistapesos))
    return valortotal

def main():
    nombre, pes, valors, pesos = map(str,demanadades())
    agafa_valoroptim(int(nombre), int(pes), valors, pesos)
    
main()

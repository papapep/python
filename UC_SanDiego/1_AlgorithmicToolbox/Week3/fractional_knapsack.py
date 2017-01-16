# Uses python3
import sys

def agafa_valoroptim(pesadmes, llistavalors, llistapesos):
    valortotal = 0.
    
#     return valortotal

# def main():
#     dadesinicials = list(map(int, sys.stdin.read().split()))
#     nombre, pesadmes = dadesinicials[0:2]
#     values = dadesinicials[2:(2 * n + 2):2]
#     weights = dadesinicials[3:(2 * n + 2):2]
#     valoroptim = agafa_valoroptim(pesadmes, pesos, valors)
#     print("{:.10f}".format(valoroptim))

def main():
    nombre, pesadmes = map(int, input().split())
    print(nombre, pesadmes)
    llistavalors = [None] * nombre
    llistapesos = [None] * nombre
    for item in range(0,nombre):
        llistavalors[item], llistapesos[item] = map(int, input().split())

main()

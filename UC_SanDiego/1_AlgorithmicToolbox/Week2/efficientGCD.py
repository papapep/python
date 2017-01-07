# -*- coding = utf-8 -*-
#After 3'' of execution, it still doesn't end...

def efficientGCD(a,b):
    if b == 0:
        return a
    
    aprima = a % b
    return efficientGCD(b, aprima)

def main():
    a = 3918848
    b = 1653264
    print(efficientGCD(a, b))

main()


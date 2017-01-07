# -*- coding = utf-8 -*-
#After 3'' of execution, it still doesn't end...

def naiveGCD(a,b):
    best = 0

    if a > b:
        inferior = b
    else: 
        inferior = a

    for nombre in range(1, inferior+1):
        if a % nombre == 0 and b % nombre == 0:
            best = nombre

    return best

def main():
    a = 412600000000000000
    b = 13203200000000000000
    print(naiveGCD(a, b))

main()


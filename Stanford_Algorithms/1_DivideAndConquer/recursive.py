# -*- coding = utf-8 -*-
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Which number do you want to calculate the factorial of?: "))
print(factorial(numero))

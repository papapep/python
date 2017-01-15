# Uses python3

def efficientGCD(a,b):
    if b == 0:
        return a
    aprima = a % b
    return efficientGCD(b, aprima)

def leastcommonmultiple(gcd, a, b):
    return (a * b) // gcd

def main():
    a, b = map(int, input().split())
    print(int(leastcommonmultiple(efficientGCD(a, b), a, b)))

main()

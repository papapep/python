# Uses python3
def fde(n, m):
    f = n % m
    return f % m

def main():
    n, m = map(int, input().split())
    print(fde(n+1, m))

main()
# Uses python3
def fiblist(num):
    f = [None] * num
    if num > 1:
        f[0] = 0
        f[1] = 1
        for element in range(2,num):
            f[element] = f[element -1] + f[element -2]
    else:
        f[0] = 0
    return(f[num-1])

def main():
    n =int(input())
    print(fiblist(n+1))

main()
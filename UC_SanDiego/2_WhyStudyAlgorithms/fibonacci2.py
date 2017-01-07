# -*- coding = utf-8 -*-
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
    n = 100000
    print(fiblist(n))

main()
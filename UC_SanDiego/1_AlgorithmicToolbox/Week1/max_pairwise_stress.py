# Uses python3
# n = int(input())
# a = [int(x) for x in input().split()]

# assert(len(a) == n)

from random import randint

try:
    while True:

        n = randint(1, 20)
        a = [randint(2, 10000) for p in range(0, n)]

        for element in a:
            print(element, end = " ")

        result = 0

        maxindex = -1
        maxindex2 = -1

        for i in range(0, n):
            if maxindex == -1 or a[i] > a[maxindex]:
                maxindex = i
        print(a[maxindex])

        for j in range(0, n):
            if (j != maxindex and maxindex2 == -1) or (j != maxindex and a[j] > a[maxindex2]):
                maxindex2 = j

        print(a[maxindex] * a[maxindex2])
        print("OK!")
except:
    print("Cagada pastoret...")

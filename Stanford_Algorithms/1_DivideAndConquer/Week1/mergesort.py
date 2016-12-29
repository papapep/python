# -*- coding= utf-8 -*-
i, j, k = 0, 0, 0
llista = [5, 4, 1, 8, 7, 2, 6, 3]
mida = (len(llista))
llistaA = [1, 4, 5, 8]
llistaB = [2, 3, 6, 7]
llistaC = [None] * mida
for volta in range(1,9):
    if llistaA[i] < llistaB[j]:
        print(volta)
        llistaC[volta] = llistaA[i]
        print(llistaC[volta])
        i += 1
        print(i)
    else:
        print(volta)
        llistaC[volta] = llistaB[j]
        print(llistaC[volta])
        j += 1
        print(j)
#print(*llistaC, sep='\n')

fhand = open('../romeo.txt')
counts = dict()
for line in fhand:
    words = line.split() #Separem les paraules de cada línia i les fiquem dins words
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items(): #Recorrem el diccionari agafant-ne els valors
    lst.append( (val,key) ) #Els afegim en posició inversa a la llista lst
lst.sort(reverse=True) #Ordenem en ordre invers la llista, el nombre major primer

for val, key in lst[:10]:
    print key, val

""" Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

name = raw_input("Enter file:")
if len(name) < 1 : name = "../mbox-short.txt"

fh = open(name)
enviaments =dict()
words =list()
hora = list()
for linia in fh:
    lini = linia.rstrip()
    if linia.startswith("From "):
        words = linia.split()
        hora = words[5]
        histo = hora.split(":")
        enviaments[histo[0]] = enviaments.get(histo[0],0) + 1
    else: continue
histog =list()

for k,v in enviaments.items():
    histog.append((k,v))
    
histog.sort()

for k,v in histog:
    print k,v


    

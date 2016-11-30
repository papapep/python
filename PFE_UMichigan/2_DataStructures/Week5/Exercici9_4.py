"""9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "../mbox-short.txt"

fh = open(fname)
adddict =dict()
words =list()
address = list()
for linia in fh:
    lini = linia.rstrip()
    if linia.startswith("From "):
        words = linia.split()
        address = words[1]
        adddict[address] = adddict.get(address,0) + 1
    else: continue
    
print address,adddict[address]

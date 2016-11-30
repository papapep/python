"""counts =dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "../mbox-short.txt"

handle = open(fname)
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
    
bigcount = None
bigword = None
for word.count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count
print bigword,bigcount

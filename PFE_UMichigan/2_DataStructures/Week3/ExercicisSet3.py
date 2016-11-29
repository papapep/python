# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
fhc = fh.read()
print fhc.upper().strip()


# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count, acc = 0,0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos=line.find(":")
    acc = acc + float(line[pos+1:])
print "Average spam confidence:",acc/count

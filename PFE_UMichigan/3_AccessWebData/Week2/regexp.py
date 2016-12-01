import re

fh = open('../regex_sum_339401.txt')
suma = 0

for line in fh:
    line = line.strip()
    found = re.findall('\d+',line)

    if len(found):
        for round in found:
            suma = suma + int(round)

print suma

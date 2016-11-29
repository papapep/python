largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
            break
    try:
        numer = int(num)
    except:
        print "Invalid input"
        continue

    if largest is None or num > numer:
        largest = numer
        
    if smallest is None or num < numer:
        smallest = numer

print "Maximum is", largest
print "Minimum is", smallest

def problem1_7():
    base1 = float(input("Enter the length of one of the bases:"))
    base2 = float(input("Enter the length of one of the other base:"))
    height = float(input("Enter the height:"))
    area = float(((base1+base2)*height)/2)
    print("The area of a trapezoid with bases",base1,"and",base2,end=" ")
    print("and height", height,"is",area)
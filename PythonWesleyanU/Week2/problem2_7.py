def problem2_7():
    """ computes area of triangle using Heron's formula. """
    side1=float(input("enter length of side one:"))
    side2=float(input("enter length of side two:"))
    side3=float(input("enter length of side three:"))
    print("Area of a triangle with sides",side1,side2,side3,"is",(.5*(side1+side2+side3)))
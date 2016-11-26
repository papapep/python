# -StartPython.py *- coding: utf-8 -*-
"""
Spyder Editor

#%% starts a new cell. Use second green triangle to run just the cell that
your mouse has last clicked in (or Ctrl-Enter on a PC or Command-Return on a
Macintosh or Menu>Run>Run Cell)
"""
#%%
def hello():
    print("Hello, world!")

#%%
def myname():
    print("My name is Bill")
    
#%%
def ourschool():
    print("Coursera is our school")

#%%  
  
""" This will run forever. In this case Ctrl-C will stop it, but sometimes
that doesn't work. In that case, click away IP Console to stop; click yes to 
kill kernel. Open a new IPConsole on the Console menu to restart """
#%%
def forever():
    while True:
        pass
  
#%% 
def areatriangle(b, h):
    print ("The area of a triangle of base " ,b ," and height " ,h , " is ", .5*b*h)

#%%
def celsius_to_fahrenheit(temp):
    """Converteix una temperatura expressada en graus Celsius a graus Fahrenheit """
    newtemp = (((9*temp)/5)+32)
    print ("The Celsius temperature ", temp , " is equivalent to ", newtemp , " degrees Fahrenheit ")
    
#%%
def name():
    """Gets your personal data and shows it in a formatted, nice format"""
    fname=raw_input("Your first name: ")
    lname = raw_input("Your last name: ")
    city = raw_input("The city where you live: ")
    country = raw_input("The country where your city is: ")
    fullname = fname + " " + lname
    location = city + ", " + country
    print "Your name is: ", fullname
    print "And you live in: ", location
    
#%%

def absolutevalue():
    
    numero = raw_input("Introdueix un nombre: ")
    
    if numero >= 0:
        valabsolut = numero
    else: 
        valabsolut = -numero
    
    print "The absolute value of ",numero," is ",valabsolut


#%%

def inches_to_feet2(inches):
    feet = inches//12
    rem_feet = inches%12
    print inches,"inches is",feet,"feet and",rem_feet,"inches"



#%%

from __future__ import print_function

def count_down():
    """Rocket count down function"""
    
    comptador = 10
    while comptador > 0:
        print (comptador, end=" ")
        comptador -= 1
    print()
    print ("BLASTOFF!")


#%%

from __future__ import print_function

def count_down1():
    """Rocket count down function"""
    
    comptador = 10
    for comptador in range(10,0,-1):
        print (comptador, end=" ")
    print()
    print ("BLASTOFF!")


#%%





























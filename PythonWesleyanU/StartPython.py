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
    
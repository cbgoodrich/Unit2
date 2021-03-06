#Charlie Goodrich
#09/14/17
#coloredSquare.py - pops up a colored square

from ggame import *
from random import randint

number = randint(1,3) #picks a random number to be assigned to a color

if number == 1: #if statements corresponding to color
    red = Color(0xff0000, 1) #hex # for red
    line = LineStyle(3, red)
    rectangle = RectangleAsset(100, 100, line, red)
    #makes the rectangle display
    Sprite(rectangle)
    myApp = App()
    myApp.run()

elif number == 2:
    blue = Color(0x191970, 1) #hex # for blue
    line = LineStyle(3, blue)
    rectangle = RectangleAsset(100, 100, line, blue)
    #makes the rectangle display
    Sprite(rectangle)
    myApp = App()
    myApp.run()
    
else:
    green = Color(0x7fffd4, 1) #hex # for green
    line = LineStyle(3, green)
    rectangle = RectangleAsset(100, 100, line, green)
    #makes the rectangle display
    Sprite(rectangle)
    myApp = App()
    myApp.run()

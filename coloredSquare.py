#Charlie Goodrich
#09/14/17
#coloredSquare.py - pops up a colored square

from ggame import *
from random import randint

number = randint(1,3) #picks a random number to be assigned to a color

if number == 1:
    red = Color(0xff0000, 1)
    line = LineStyle(3, red)
    rectangle = RectangleAsset(100, 100, line, red)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
    

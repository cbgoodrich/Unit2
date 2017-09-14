#Charlie Goodrich
#09/13/17
#insulter.py - insults you to your core

from random import randint

input("Enter your name: ")

number = randint(1,5)
if number == 1:
    print("You eat cereal with a fork")
elif number == 2:
    print("You don't know how to commit your files")
elif number == 3:
    print("I've owned dogs smarter than you")
elif number == 4:
    print("You don't know the difference between an integer and a float")
else:
    print("You can't correctly write an 'if' statement")

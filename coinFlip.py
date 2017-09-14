#Charlie Goodrich
#09/13/17
#coinFlip.py - tells you heads or tails

from random import randint

number = randint(1,2)
print("Flipping your coin...")
if number == 2:
    print("Tails")

else:
    print("Heads")

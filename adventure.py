#Charlie Goodrich
#09/13/17
#adventure.py - models the 1976 game 'Adventure'

print("A bear is chasing you")
print("You come to a river")
riverYOrN = input("Do you jump in the river? ")
if riverYOrN == "yes":
    print("Thankfully you know how to swim")
    print("However, you notice a nearby shark")
    sharkYOrN = input("Do you punch it in the nose? ")
    if sharkYOrN == "yes":
        print("The shark eats you, and you die :(")
    else:
        print("The shark swims away, only to eat you later")
else:
    print("The bear eats you :(")
    
    


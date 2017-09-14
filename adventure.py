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
        print("You befriend the shark")
        print("Soon you become hungy, your stomach is rumbling")
        soupYOrN = input("Do you want to make sharkfin soup? ")
        if soupYOrN == "yes":
            print("The shark eats you before you can kill it. It's hungry too :(")
        else:
            print("You die of starvation :(")
else:
    print("You fall off a cliff while running from the bear. You're dead :(")
    


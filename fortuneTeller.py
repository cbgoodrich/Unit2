#Charlie Goodrich
#09/13/17
#fortuneTeller.py - tells you your fortune

color = input("Pick red or blue: ")
number = int(input("Enter a number from 1-4: "))

if color == "red" and number == 1:
    print("You will win the lottery, but ultimately become bankrupt")
elif color == "red" and number == 2:
    print("You will die tragically in a bird accident")
elif color == "red" and number == 3:
    print("You will discover the cure for cancer")
elif color == "red" and number == 4:
    print("Someone will take the credit for all of your accomplishments")
elif color == "blue" and number == 1:
    print("You will become a professional baseball player at the age of 70")
elif color == "blue" and number == 2:
    print("You will take the credit all of the work that the person who",
                                    "selected 'red' and '4' did")
elif color == "blue" and number == 3:
    print("You children will be eaten by a giant fish like in Finding Nemo")
else:
    print("You will be attacked by a bear")
#Charlie Goodrich
#09/14/17
#lastname.py - tells you which half of the alphabet your name is in

last_name = input("Enter your last name: ")
lastName = last_name.lower()
if lastName > "a" and lastName < "m":
    print("Your name is in the first half of the alphabet")
else:
    print("Your name is the the second half of the alphabet")


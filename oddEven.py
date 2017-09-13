#Charlie Goodrich
#09/13/17
#oddEven.py - tells you if your number is odd or even

number = int(input("Enter a number: "))

remainder = number % 2

if remainder != 0:
    print(number, "is odd")
else:
    print(number, "is even")

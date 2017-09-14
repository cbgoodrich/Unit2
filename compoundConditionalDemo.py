#Charlie Goodrich
#09/14/17
#compoundConditionalDemo.py - and/or

number = float(input("Enter a number: "))

if number > 0 and number%7 == 0:
    print("Your number is positive and divisible by seven")
elif number > 0:
    print("Your number is positive but not divisible by seven")
elif number < 0 and number%7 == 0:
    print("Your number is negative and divisible by seven")
elif number < 0:
    print("Your number is negative but not divisible by seven")
else:
    print("Your number is zero")

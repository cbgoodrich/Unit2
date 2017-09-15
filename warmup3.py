#Charlie Goodrich
#09/15/17
#warmup.py - tells you if input is divisible by 2 and 3

number = int(input("Enter a number: "))

if number%3 == 0 and number%2 == 0:
    print("Your number is divisible by 2 and 3")
elif number%3 == 0:
    print("Your number is divisible by 3")
elif number%2 == 0:
    print("Your number is divisible by 2")
else:
    print("Your number is divisible by neither")

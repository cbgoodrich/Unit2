#Charlie Goodrich
#09/25/17
#quiz2.py - my second quiz

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

product = num1 * num2

if num1 == num2:
    print("The numbers are the same")
elif num1 > num2:
    print("The first number is bigger")
else:
    print("The second number is bigger")

if num1%3 == 0 and num2%3 == 0:
    print("Both are divisible my 3")
elif num1%3 == 0 and num2%3 != 0:
    print("Only the first is divisible by 3")
elif num1%3 != 0 and num2%3 == 0:
    print("Only the second is divisible by 3")
else:
    print("Neither number is divisible by 3")

productGuess = float(input("What is the product of your two numbers? "))
if product == productGuess:
    print("Correct")
else:
    print("Incorrect")


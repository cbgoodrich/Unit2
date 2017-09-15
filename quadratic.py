#Charlie Goodrich
#09/15/17
#quadratic.py - gives you the solution to your quadratic

from math import sqrt

print("ax^2 + bx + c = 0")
a = float(input("Enter an a-value: ")) #a-value of quadratic
b = float(input("Enter a b-value: ")) #b-value of quadratic
c = float(input("Enter a c-value: ")) #c-value of quadratic

if sqrt(b**2 - 4*a*c) >= 0: #testing if the determinate is greater than 0
    x1 = (-b + sqrt((b**2 - 4*a*c))/2*a
    x2 = (-b - sqrt((b**2 - 4*a*c))/2*a
    print("X =", x1)
    print("X =", x2)
else:
    real = (-b)/2a
    imaginary = sqrt((abs(b**2 - 4*a*c)))/2*a
    print("X =", real, "+", imaginary, "i")
    print("x =", real, "-", imaginary, "i")
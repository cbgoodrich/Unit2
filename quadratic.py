#Charlie Goodrich
#09/15/17
#quadratic.py - gives you the solution to your quadratic

from math import sqrt

print("ax^2 + bx + c = 0")
a = float(input("Enter an a-value: ")) #a-value of quadratic
b = float(input("Enter a b-value: ")) #b-value of quadratic
c = float(input("Enter a c-value: ")) #c-value of quadratic

if (b**2 - 4*a*c) >= 0: #testing if the determinate positive
    x1 = (-b/(2*a)) + (sqrt(b**2 - (4*a*c)))/(2*a)
    x2 = (-b/(2*a)) - (sqrt(b**2 - (4*a*c)))/(2*a)
    print("X =", x1)
    print("X =", x2)
else:
    real = (-b)/(2*a)
    imaginary = sqrt(abs(b**2 - (4*a*c)))/(2*a)
    print("X =", real, "+", imaginary, "i")
    print("x =", real, "-", imaginary, "i")
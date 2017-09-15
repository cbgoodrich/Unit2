#Charlie Goodrich
#09/15/17
#slope.py - calculates slope and the equation of a line

x1 = float(input("x1= "))
y1 = float(input("y1= "))
x2 = float(input("x2= "))
y2 = float(input("y2= "))

if x1-x2 == 0:
    print("The slope of your undefined")
    print("The equation of your line is X=", x1)
else:
    slope = float((y2-y1)/(x2-x1))
    yIntercept = float(y1-slope*x1)
    
    print("The slope of the line is", slope)
    print("The equation of the line is Y =", slope, "x +", yIntercept)


#Charlie Goodrich
#09/13/17
#gradeCalculator.py - tells you your grade

grade = int(input("What is your grade? "))

if grade <= 100 and grade >=90:
    print("You have an A")
elif grade < 90 and grade >= 80:
    print("You have a B")
elif grade < 80 and grade >=70:
    print("You have a C")
elif grade < 70 and grade >= 60:
    print("You have a D")
else:
    print("You're failing :(")


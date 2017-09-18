#Charlie Goodrich
#09/15/17
#ageCalculator.py - calculates how old you are

from datetime import date
import sys
year = int(input("Enter the year you were born in: "))
month = int(input("Enter the month you were born in: "))
day = int(input("Enter the day you were born on: "))

if month > 12:
    print("Start again, and enter a real month")
    quit()

yearNow = date.today().year
monthNow = date.today().month
dayNow = date.today().day

if monthNow < month:
    print("You are", yearNow - year - 1, "years old")
elif monthNow == month:
    if dayNow < day:
        print("You are", yearNow - year - 1, "years old")
    else:
        print("You are", yearNow - year, "years old")
else:
    print("You are", yearNow - year, "years old")

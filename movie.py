#Charlie Goodrich
#09/13/17
#movie.py - asks the user's age, prints the type of movies they can watch

age = int(input("What is your age? "))

if age >= 13 and age < 17:
    print("You can watch PG-13 movies")
elif age >= 17:
    print("You can watch PG-13 movies and R movies")
else:
    print("You can watch PG and G movies")

#write a program to print to ask for a name and age.when oth values have been entered, check if the
#person is the right age to go on an 18-30 holiday.
#If the person is under 18, print a message saying they are too young.

from os import name


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age <= 30:
    print(f"Welcome {name}! You are eligible for the 18-30 holiday.")
elif age < 18:
    print(f"Sorry {name}, you are too young for this holiday.")
else:
    print(f"Sorry {name}, you are not eligible for this holiday.")

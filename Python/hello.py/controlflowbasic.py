#a code that checks if a user is valid for a drivers licenece

name = input("what is your name? ")
age = int(input(" hi {0} how old are you? " .format(name)))
print("you are {} years old"  .format(age))

if age >= 18:
    print("you are legible to drive {0} ".format(name))

else:
    print("you are under age {1} ,please come back in {0} years ".format(18-age , name))


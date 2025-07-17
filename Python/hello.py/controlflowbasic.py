#program that checks idf a given number is "special",a number is special its divible by 5 or 3 
#not both at the same time

number = int(input("insert number: "))

if (number % 3 == 0 or number % 5==0) and not (number % 3 == 0 and number % 5==0):
     print("special")
else:
     print("not special")
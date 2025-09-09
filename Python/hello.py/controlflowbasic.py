user_input = input ("please enter 3 numberss separated by commas: ")

numbers = user_input.split(",")
a = int(numbers[0])
b = int(numbers[1]) 
c = int(numbers[2])

result = a + b - c
print ("The result is: " + str(result))
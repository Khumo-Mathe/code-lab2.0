
Number = int(input("Enter a number: "))
if Number > 100:
    print("number too high, enter number lower than 100")
else:
    for num in range(1, Number + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
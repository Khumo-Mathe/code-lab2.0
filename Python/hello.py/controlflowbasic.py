# FizzBuzz function that returns a list of FizzBuzz results
from typing import List


def fizzbuzz( number : int) -> List[str]:
    result = []

    

    for num in range(1, number + 1):
        if num % 5 == 0 and num % 3 == 0:
            result.append("fizzbuzz")  
        elif num % 3 == 0:
            result.append("fizz")                            
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(num))
    return result
number = int(input("enter number: "))

print(fizzbuzz(number))  # Print the result of the fizzbuzz function
answer = 5
print("please guess a number between 1 and 10:")

guess = int(input())

if guess > answer:
    print("guess lower")
elif guess < answer:
    print("guess higher")
else :
    print("CORRECT")
   

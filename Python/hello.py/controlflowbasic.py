low = 1
high = 1000

print(f"please think of a number between {low} and {high}")
input("please press enter to start")

guess =1 

while True:
    guess = low + (high - low) // 2
    high_low = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").strip().upper()
    if high_low == "H":
        print(f"Your number is between {low} and {guess - 1}")
    
    elif high_low == "L":
        print(f"Your number is between {guess + 1} and {high}")
        low = guess + 1
    elif high_low == "C":
        print(f"Your number is {guess}!")
        break
    else:
        print("Please enter H, L, or C")

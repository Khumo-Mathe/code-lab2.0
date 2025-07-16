answer=5
guess=int(input())

if answer>guess:
    print ("please guess higher")
    guess=int(input())
    if answer==guess:
        print("guess is correct")
    else:
        print("sorry guess was in correct")
elif answer<guess:
    print("please guess lower")
    guess=int(input())
    if answer==guess:
        print("answer is correct")
    else:
        print("sorry guess was incorrect")
else:
    print("guess is correct")
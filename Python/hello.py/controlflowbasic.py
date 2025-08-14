#count and say function
def count_and_say(n: int)-> str:
    if n == 1:
        return "1"
    current_term ="1"
    
    for _ in range(2 ,n + 1 ):
        next_term = ""
        count = 1
        
        for i in range(1 , len(current_term)):
            if current_term [i] == current_term[i - 1]:
                count += 1
            else:
                next_term += str(count) + current_term[i - 1]
                count = 1
                
        next_term += str(count) + current_term[-1]
        current_term = next_term
    
    
    return current_term
n = int(input("enter a number  :"))
result = count_and_say(n)
print(result)
        
        
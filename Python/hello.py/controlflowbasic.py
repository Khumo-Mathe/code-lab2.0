class  solution :
    def largestgoodinterger(num:str):
        max_good = ""
        
        for i in range(0,len(num)-3):
            sub = num [i : i + 3]
            if sub[0] == sub[1] == sub [2]:
                if sub > max_good:
                    max_good = sub
        return max_good            
                
        
        
        
        
      
    


        
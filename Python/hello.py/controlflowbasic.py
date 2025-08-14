def SouthAfrica():
    capital_city={
        "Gauteng" :"johannesburg",
        "NorthWest" : "mahikeng",
        "NorthenCape" : "kimberly",
        "WesternCape" : "capetown",
        "EasternCape" : "eastlondon",
        "KwaZuluNatal" : "durban",
        "Mpumalanga" : "nelspruit",
        "FreeState" : "bloemfontein",
        
        
    }
    
    province = input("enter province to get the capital city: ")
    
    capital = capital_city.get(province,"capital not found")
    print(f"the capital of {province} is :  {capital}")
SouthAfrica()  
    
    


        
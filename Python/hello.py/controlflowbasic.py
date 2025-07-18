#password strength checker
password = input("Enter your password: ")

def check_password_strength(password):

    if len(password) < 8:
        return "Weak password: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak password: Password must contain at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak password: Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak password: Password must contain at least one lowercase letter."
    else:
      
        return "Strong password."
    
print(check_password_strength(password))
  
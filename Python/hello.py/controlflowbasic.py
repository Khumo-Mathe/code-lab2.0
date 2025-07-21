#grade categorizer

grade = int(input("Enter your grade: "))

def categorize_grade(grade):
    if grade >= 75:
        return "distinction"
    elif grade >= 60 and grade < 75:
        return "merit"
    elif grade >= 50 and grade < 60:
        return "pass"
    elif  grade < 50:
        return "fail"
    else:
        return "F"
print("Your grade is:", categorize_grade(grade))
  
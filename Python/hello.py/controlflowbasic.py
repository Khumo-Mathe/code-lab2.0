#grade categorizer

grade = int(input("Enter your grade: "))

def categorize_grade(grade):
    if grade >= 75:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
  
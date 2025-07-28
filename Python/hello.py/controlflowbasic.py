fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    if fruit == "date":
        continue
    print(f"I like {fruit}") # This will skip printing "date" and continue with the next fruit

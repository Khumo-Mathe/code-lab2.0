fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruit_to_find = "cherry"
index = None

for index in range(len(fruits)):
    if fruits[index] == fruit_to_find:
        print(f"Found {fruit_to_find} at index {index}")
        break # If found, exit the loop                  
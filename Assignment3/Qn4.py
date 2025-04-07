# List of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Writing names to the file
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Reading and printing names from the file
with open("names.txt", "r") as file:
    print("Names in the file:")
    for line in file:
        print(line.strip())  # Remove trailing newline characters
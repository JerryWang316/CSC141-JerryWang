# Create learning_python.txt file
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can create variables to store data.\n")
    file.write("In Python you can use loops to repeat actions.\n")
    file.write("In Python you can define functions to organize code.\n")
    file.write("In Python you can work with lists, tuples and dictionaries.\n")
    file.write("In Python you can read from and write to files.\n")

    # 10-3. Simpler Code - Original version with temporary variable
print("=== Original version with temporary variable ===")
with open('learning_python.txt') as file:
    contents = file.read()
    lines = contents.splitlines()
    for line in lines:
        print(line)

print("\n=== Simplified version without temporary variable ===")
with open('learning_python.txt') as file:
    contents = file.read()
    for line in contents.splitlines():
        print(line)
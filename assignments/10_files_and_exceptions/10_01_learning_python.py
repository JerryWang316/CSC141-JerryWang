# Create learning_python.txt file
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can create variables to store data.\n")
    file.write("In Python you can use loops to repeat actions.\n")
    file.write("In Python you can define functions to organize code.\n")
    file.write("In Python you can work with lists, tuples and dictionaries.\n")
    file.write("In Python you can read from and write to files.\n")

    # 10-1. Learning Python
print("=== Reading the entire file at once ===")
with open('learning_python.txt') as file:
    contents = file.read()
    print(contents)

print("\n=== Reading the file line by line ===")
with open('learning_python.txt') as file:
    for line in file:
        print(line.rstrip())
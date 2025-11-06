# Create learning_python.txt file
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can create variables to store data.\n")
    file.write("In Python you can use loops to repeat actions.\n")
    file.write("In Python you can define functions to organize code.\n")
    file.write("In Python you can work with lists, tuples and dictionaries.\n")
    file.write("In Python you can read from and write to files.\n")

    # 10-2. Learning C
print("=== Replacing 'Python' with 'C' ===")
with open('learning_python.txt') as file:
    for line in file:
        modified_line = line.replace('Python', 'C')
        print(modified_line.rstrip())
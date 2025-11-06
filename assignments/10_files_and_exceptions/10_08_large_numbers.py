# 10-8. Cats and Dogs
# First, create the files
with open('cats.txt', 'w') as file:
    file.write("Whiskers\n")
    file.write("Mittens\n")
    file.write("Shadow\n")

with open('dogs.txt', 'w') as file:
    file.write("Buddy\n")
    file.write("Max\n")
    file.write("Bella\n")

# Now read and display the files
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")
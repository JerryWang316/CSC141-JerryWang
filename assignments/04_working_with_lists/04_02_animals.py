animals = ['dog', 'cat', 'rabbit']

print("Animal names:")
for animal in animals:
    print(animal)

print("\n")

print("Statements about each animal:")
for animal in animals:
    if animal == 'dog':
        print(f"A {animal} would make a great pet.")
    elif animal == 'cat':
        print(f"A {animal} is independent and low maintenance.")
    elif animal == 'rabbit':
        print(f"A {animal} is quiet and gentle.")

print("\n")

print("Any of these animals would make a great pet!")
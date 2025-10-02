# Create several pet dictionaries
pet1 = {'animal': 'dog','owner': 'Alice'}

pet2 = {'animal': 'cat','owner': 'Bob'}

pet3 = {'animal': 'parrot','owner': 'Charlie'}

pet4 = {'animal': 'hamster','owner': 'Diana'}

pet5 = {'animal': 'goldfish','owner': 'Ethan'}

# Store all pet dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4, pet5]

# Loop through the list and print all information about each pet
print("Pet Information:")
print("=" * 30)

for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print("-" * 20)
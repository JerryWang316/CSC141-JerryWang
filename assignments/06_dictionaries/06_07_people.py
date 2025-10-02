# Create three person dictionaries
person1 = {'first_name': 'Tianrui','last_name': 'Wang','age': 20,'city': 'Hong Kong'}

person2 = {'first_name': 'Seyeon','last_name': 'Jeong','age': 21,'city': 'Seoul'}

person3 = {'first_name': 'Maddie','last_name': 'Wood','age': 18,'city': 'New York'}

# Store all dictionaries in a list called people
people = [person1, person2, person3]

# Loop through the list of people and print all information
print("People Information:")
print("=" * 50)

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("-" * 30)
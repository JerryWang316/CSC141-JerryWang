# Create a dictionary of favorite places
favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['Barcelona', 'Rome'],
    'Charlie': ['Bali', 'Sydney', 'Rio de Janeiro', 'London'],
    'Diana': ['Kyoto'],
    'Ethan': ['Berlin', 'Amsterdam']}

print("Favorite Places:")
print("=" * 40)

# Loop through the dictionary and print each person's favorite places
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places:")
    
    # Check if there's only one place or multiple places
    if len(places) == 1:
        print(f"  - {places[0]}")
    else:
        for place in places:
            print(f"  - {place}")
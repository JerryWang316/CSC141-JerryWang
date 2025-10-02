# Create a dictionary of cities with nested dictionaries
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 37_400_000,
        'fact': 'Tokyo is the most populous metropolitan area in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': 2_161_000,
        'fact': 'Paris is known as the "City of Light" (La Ville Lumière).'
    },
    'New York': {
        'country': 'United States',
        'population': 8_400_000,
        'fact': 'The Statue of Liberty was a gift from France in 1886.'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': 9_500_000,
        'fact': 'Cairo is home to the Great Pyramids of Giza.'
    },
    'Sydney': {
        'country': 'Australia',
        'population': 5_312_000,
        'fact': 'Sydney Opera House was designed by Danish architect Jørn Utzon.'
    }}

print("Cities Information")
print("=" * 50)

# Loop through the cities dictionary and print all information
for city, info in cities.items():
    print(f"\n{city.upper()}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")
    print("-" * 50)
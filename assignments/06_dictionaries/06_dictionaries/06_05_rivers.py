rivers = {'nile': 'egypt','amazon': 'brazil','yangtze': 'china', 'mississippi': 'united states','danube': 'germany'}

print("Rivers and Countries:")
print("=" * 30)

print("\n1. Sentences about each river:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n2. Names of each river:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n3. Names of each country:")
for country in rivers.values():
    print(f"- {country.title()}")
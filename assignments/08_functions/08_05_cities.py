def describe_city(city, country="Iceland"):
    """Print a sentence describing a city and its country"""
    print(f"{city} is in {country}.")

# Call function for three different cities
describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("Paris", "France")
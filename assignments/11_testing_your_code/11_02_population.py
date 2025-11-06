def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    
    from city_functions import city_country

def test_city_country():
    formatted_string = city_country('santiago', 'chile')
    assert formatted_string == 'Santiago, Chile'

def test_city_country_population():
    formatted_string = city_country('santiago', 'chile', 5000000)
    assert formatted_string == 'Santiago, Chile - population 5000000'
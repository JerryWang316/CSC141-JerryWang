def city_country(city, country):
    return f"{city.title()}, {country.title()}"

def test_city_country():
    formatted_string = city_country('santiago', 'chile')
    assert formatted_string == 'Santiago, Chile'
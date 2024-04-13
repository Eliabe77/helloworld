def city_country(city, country):
    """Return a string like 'Lugano, Switzerland'."""
    return f"{city.title()}, {country.title()}"

city = city_country('punta arenas', 'chile')
print(city)

city = city_country('Oslo', 'norvegia')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
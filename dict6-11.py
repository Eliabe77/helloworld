cities = {
    'Punta Arenas': {
        'country': 'cile',
        'population': 130704,
        'nearby mountains': 'Cordigliera andina',
        },
    'Santa Barbara': {
        'country': 'California',
        'population': 88000,
        'nearby mountains': 'Santa Ynes',
        },
    'Hong Kong': {
        'country': 'Cina',
        'population': 7000000,
        'nearby mountains': 'Victoria peak',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
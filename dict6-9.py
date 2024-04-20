favorite_places = {
    'Elia': ['Sharm', 'Viareggio', 'Bejing'],
    'George': ['Lourdes', 'Berlin', 'London'],
    'Joseph': ['Cogoleto', 'Provence', 'Split']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())
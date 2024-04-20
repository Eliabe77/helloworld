favorite_numbers = {
    'Elia': [42, 17],
    'Michele': [42, 39, 56],
    'Mary': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))
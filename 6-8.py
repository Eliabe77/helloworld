# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'cat',
    'name': 'Milu',
    'owner': 'Elia',
    'weight': 38,
    'eats': 'birds',
}
pets.append(pet)

pet = {
    'animal type': 'rabbit',
    'name': 'Claire',
    'owner': 'Elia',
    'weight': 4,
    'eats': 'hay',
}
pets.append(pet)

pet = {
    'animal type': 'lion',
    'name': 'Tod',
    'owner': 'Mom',
    'weight': 71,
    'eats': 'everything',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
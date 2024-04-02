# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'Barbara',
    'last_name': 'Lewis',
    'age': 43,
    'city': 'Singapour',
    }
people.append(person)

person = {
    'first_name': 'Loris',
    'last_name': 'Mattew',
    'age': 25,
    'city': 'London',
    }
people.append(person)

person = {
    'first_name': 'Tom',
    'last_name': 'Jefferson',
    'age': 18,
    'city': 'Tourin',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")
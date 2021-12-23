pets = {
    'olive': {
        'animal': 'dog',
        'type': 'labrador retriever',
        'gender': 'female',
        'color': 'black',
    },

    'sugar': {
        'animal': 'rodent',
        'type': 'gerbil',
        'gender': 'female',
        'color': 'white',
    },

    'spice': {
        'animal': 'rodent',
        'type': 'gerbil',
        'gender': 'female',
        'color': 'black',
    },
}

for pet, info in pets.items():
    if pet == 'olive':
        print(f"We have a {info['animal']} named {pet.title()}. She's {info['gender']} and is a {info['color']} {info['type']}.")
    else:
        print(f"We used to have a {info['animal']} named {pet.title()}. She's {info['gender']} and was a {info['color']} {info['type']}.")
family = {
    'sister': {
        'first': 'zoe',
        'last': 'morken',
        'age': 21,
        'city': 'broomfield',
    },

    'mother': {
        'first': 'hua',
        'last': 'morken',
        'age': 49,
        'city': 'broomfield',
    },

    'father': {
        'first': 'paul',
        'last': 'morken',
        'age': 51,
        'city': 'broomfield',
    },
}

# my_sister = {'first_name': 'zoe', 'last_name': 'morken', 'age': '21', 'city': 'broomfield'}
#
# print(my_sister['first_name'].title())
# print(my_sister['last_name'].title())
# print(my_sister['age'])
# print(my_sister['city'].title())

for person, info in family.items():
    print(f"My {person}'s name is {info['first'].title()} {info['last'].title()}, who is {info['age']} years old and lives in {info['city'].title()}.")
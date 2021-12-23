favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

for name in favorite_languages.keys():
    print(f"{name.title()}, thank you for taking the poll.")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\nChecking list of people who are required to take the poll...")
should_take_poll = ['jen', 'jack', 'eva', 'david']
for name in should_take_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, you still haven't taken the poll!")
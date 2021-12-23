favorite_numbers = {
    'noah': ['37', '100'],
    'gabe': ['2'],
    'ed': ['1'],
    'ramanujan': ['1729'],
    'sigma': ['11', '8', '4', '2', '6', '3'],
}

# print(f"Noah's favorite number is {favorite_numbers['noah']}.")
# print(f"Gabe's favorite number is {favorite_numbers['gabe']}.")
# print(f"Ed's favorite number is {favorite_numbers['ed']}.")
# print(f"Ramanujan's favorite number is {favorite_numbers['ramanujan']}.")
# print(f"Sigma's favorite number is {favorite_numbers['sigma']}.")

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    for number in numbers:
        print(f"\t{number}")
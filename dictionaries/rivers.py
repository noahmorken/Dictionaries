rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon river': 'brazil',
    'river thames': 'england',
    'missisippi river': 'united states',
}

for river, country in rivers.items():
    if country != 'united states':
        print(f"The {river.title()} runs through {country.title()}.")
    else:
        print(f"The {river.title()} runs through the {country.title()}.")

print("\nRivers mentioned:")
for river in rivers.keys():
    print(river.title())

print("\nCountries mentioned:")
for country in rivers.values():
    print(country.title())
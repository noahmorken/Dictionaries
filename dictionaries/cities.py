cities = {
    'paris': {
        'country': 'france',
        'population': '2.161 million',
        'fact': 'it is known for its cafe culture alongside the Eiffel Tower and the Notre-Dame cathedral',
    },

    'macau': {
        'country': 'china',
        'population': '640,445',
        'fact': 'it was a Portuguese territory until 1999',
    },

    'delhi': {
        'country': 'india',
        'population': 'million',
        'fact': 'it dates back to the 1600s and holds the impressive Red Fort',
    },
}

for city, info in cities.items():
    print(f"{city.title()} is located in {info['country'].title()}. It has a population of {info['population']} and {info['fact']}.")
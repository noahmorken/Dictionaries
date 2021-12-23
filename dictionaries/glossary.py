glossary = {
    'glossary': 'alphabetical list',
    'variable': 'label value',
    'loop': 'repeat instructions',
    'dictionary': 'store related information',
    'syntax': 'layout',
    'set': 'uniques only',
    'keys': 'labels in dictionaries',
    'values': 'assigned meaning of keys',
    'items': 'keys and values',
    'sneed': 'formerly chuck\'s',
}

# print(f"Glossary: {glossary['glossary']}")
# print(f"Variable: {glossary['variable']}")
# print(f"Loop: {glossary['loop']}")
# print(f"Dictionary: {glossary['dictionary']}")
# print(f"Syntax: {glossary['syntax']}")

for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
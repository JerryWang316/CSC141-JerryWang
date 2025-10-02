# Programming glossary with initial terms
glossary = {
    'variable': 'A named storage location in memory that holds a value which can be changed during program execution.',
    'function': 'A block of organized, reusable code that performs a single, related action.',
    'list': 'A built-in Python data structure that holds an ordered collection of items, which can be of different types.',
    'loop': 'A programming construct that repeats a block of code multiple times until a specified condition is met.',
    'dictionary': 'A collection of key-value pairs that allows efficient data retrieval based on unique keys.'}

print("Programming Glossary")
print("=" * 50)

# Loop through the dictionary to print all terms
for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"  {meaning}")

# Add five more Python terms
glossary['string'] = 'A sequence of characters surrounded by quotes, used to represent text in programs.'
glossary['integer'] = 'A whole number without decimals, which can be positive, negative, or zero.'
glossary['float'] = 'A number that has a decimal point or is written in exponential form.'
glossary['boolean'] = 'A data type that can only have one of two values: True or False.'
glossary['comment'] = 'Text in the code that is ignored by the interpreter, used to explain code to human readers.'

print("\n" + "=" * 50)
print("UPDATED GLOSSARY (with 5 new terms)")
print("=" * 50)

# Loop through the updated dictionary
for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"  {meaning}")
glossary = {'variable': 'A named storage location in memory that holds a value which can be changed during program execution.'
            ,'function': 'A block of organized, reusable code that performs a single, related action.'
            ,'list': 'A built-in Python data structure that holds an ordered collection of items, which can be of different types.'
            ,'loop': 'A programming construct that repeats a block of code multiple times until a specified condition is met.'
            ,'dictionary': 'A collection of key-value pairs that allows efficient data retrieval based on unique keys.'}

print("Programming Glossary")
print("=" * 50)

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"  {meaning}")
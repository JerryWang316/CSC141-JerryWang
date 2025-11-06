# 10-10. Common Words
# First, let's create a sample text file for demonstration
sample_text = """
The quick brown fox jumps over the lazy dog. The dog barked at the fox.
Then the fox ran away. There were many trees in the forest.
The end of the story is that the fox found a new home.
"""

with open('sample_text.txt', 'w') as file:
    file.write(sample_text)

# Now analyze the text
filename = 'sample_text.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
        
    # Count 'the' (any case)
    count_the = contents.lower().count('the')
    print(f"The word 'the' appears {count_the} times in {filename} (case-insensitive).")
    
    # Count 'the ' (with space, to avoid counting words like 'then')
    count_the_space = contents.lower().count('the ')
    print(f"The word 'the ' (with space) appears {count_the_space} times in {filename}.")
    
    # Show the difference
    difference = count_the - count_the_space
    print(f"There are {difference} instances where 'the' is part of another word.")
    
except FileNotFoundError:
    print(f"Sorry, the file {filename} was not found.")
# Dictionary from favorite_languages.py
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'rust','phil': 'python',}

# List of people who should take the poll
poll_respondents = ['jen', 'sarah', 'edward', 'phil', 'john', 'emma']

# Loop through the list of people
for person in poll_respondents:
    if person in favorite_languages:  # Check if the person is a key in the dictionary:cite[2]:cite[5]:cite[9]
        language = favorite_languages[person].title()
        print(f"Thank you, {person.title()}, for responding to the poll! We see you love {language}.")
    else:
        print(f"{person.title()}, we invite you to take the favorite languages poll.")
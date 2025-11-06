# 10-9. Silent Cats and Dogs
filenames = ['cats.txt', 'dogs.txt', 'birds.txt']  # birds.txt doesn't exist

for filename in filenames:
    try:
        with open(filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)
    except FileNotFoundError:
        pass  # Fail silently - do nothing if file is missing
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato", "mayo")
make_sandwich("peanut butter", "jelly")
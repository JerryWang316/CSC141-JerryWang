def make_shirt(size="large", text="I love Python"):
    """Print shirt size and the message printed on it with default values"""
    print(f"The shirt size is {size} and it has the message: '{text}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt("medium")

# Any size with different message
make_shirt("small", "Python is awesome!")
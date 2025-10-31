def make_shirt(size, text):
    """Print shirt size and the message printed on it"""
    print(f"The shirt size is {size} and it has the message: '{text}'")

# Call function using positional arguments
make_shirt("Large", "I love Python!")

# Call function using keyword arguments
make_shirt(size="Medium", text="Hello World!")
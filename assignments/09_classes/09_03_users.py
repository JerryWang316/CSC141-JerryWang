# 9-3. Users
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print(f"User Information:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back.")

user1 = User("John", "Doe", 30, "New York")
user2 = User("Alice", "Smith", 25, "London")
user3 = User("Bob", "Johnson", 35, "Tokyo")

user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()
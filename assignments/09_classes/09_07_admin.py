# First, define the base classes that will be inherited
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User Information:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


# 9-7. Admin
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user", "can manage users"]
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Alice", "Smith", 35, "Admin Office")
admin.show_privileges()
print()
# user_module.py
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

# admin_module.py

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can manage users"]
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

# 9-12_main.py

admin = Admin("Alice", "Smith", 35, "Head Office")
admin.privileges.show_privileges()
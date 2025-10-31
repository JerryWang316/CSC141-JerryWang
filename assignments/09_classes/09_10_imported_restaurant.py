# restaurant_module.py
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']
    
    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# 9-10_main.py

my_restaurant = Restaurant("The Great Plate", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
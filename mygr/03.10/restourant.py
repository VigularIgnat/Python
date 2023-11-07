class Restourant:
    def __init__(self, resturant_name,kitchen_type):
        self.resturant_name=resturant_name
        self.kitchen_type=kitchen_type
    def describe_restaurant(self):
        print(f"Your name of restourant{self.resturant_name} \t type of restourant-{self.kitchen_type}")
    def open_restourant(self):
        print(f"{self.resturant_name} is closed")
            

my_restour=Restourant("Chacha","Georgian")
my_restour.describe_restaurant()
my_restour.open_restourant()

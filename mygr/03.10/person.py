class User:
    
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe(self):
        information=f"{self.first_name} {self.last_name} is user in our team"
        print(information)
    def greet_user(self):
        wish=f"Ms {self.first_name} {self.last_name} i would like to celebeate you"
        print(wish)
artem=User("Artem","Bucksin")
artem.describe()
artem.greet_user()
sasha=User("Sasha","Gridyn")
sasha.describe()
sasha.greet_user()

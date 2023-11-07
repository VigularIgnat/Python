class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def full_info(self):
        full_information=f"Name-{self.name} age -{self.age}"
        print(full_information)
        
name_second=input("Write name")
age_second=int(input("Write age"))
frolova_nata=People(name_second,age_second)

frolova_nata.full_info()

class Car:
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
        self.odometer_reader=200_000
    def full_information(self):
        full_information=f'''Model's car-{self.model}
year:{self.year}
car's color:{self.color}
odometer-{self.odometer_reader}
'''
        print(full_information)
        
    def update(self,agemiles):
        if self.odometer_reader>agemiles:
            print("ERROR")
        else:
            self.odometer_reader=agemiles
class Electrocar(Car):
    def __init__(self,model,year,color):
        super().__init__(model,year,color)

class Tesla(Electrocar):
    
        
my_car=Car("audi-q8","2000","black")
my_car.update(100_000)

my_car.full_information()

my_tesla=Electrocar("model-x","2018","white")

my_tesla.full_information()

import random

class Die:
    def __init__(self):
        self.sides=6
    def roll_die(self):
        self.number=random.randint(1,self.sides)
        print(self.number)
    def update(self,sides):
        self.sides=sides
        
make_die=Die()
make_die.roll_die()


die_first=Die()
die_first.update(10)

die_second=Die()
die_second.update(20)


for i in range(11):
    die_first.roll_die()
    die_second.roll_die()

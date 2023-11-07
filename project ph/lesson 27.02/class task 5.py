class Klass_1:
    predm="informatika"
    clas=8
    def func_1(self,a1):
        self.predmet=a1
    def func_2(self,a2):
        self.clas=a2
        
ob1=Klass_1()
ob2=Klass_1()
print(ob1.predm,ob1.clas)

ob1.func_1("mathematics")
ob1.func_2(10)
print(ob1.predmet,ob1.clas)

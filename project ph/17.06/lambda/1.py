h=10
def func1(x,y):
    return (x+y)*2
    
print(func1(5,8))

rez= lambda x,y:(x+y)*2
print(rez(5,9))

t=lambda: (5+7)*9

print(t())

r= lambda x,y,z: ((x+y)*3)*z
print(r(10,2,3))


a1=lambda: 5*7+9
a2= lambda x,y: x*x+y/2
a3= lambda x,y,z=3:x/y+z*2
a4= lambda x,y,z:x*2+y*2+z*2
print(a1())
print(a2(7,8))

print(a3(6,7))
print(a4(8,9,3))

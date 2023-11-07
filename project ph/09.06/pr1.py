def convert(s,kurs):
    return s/kurs

def convert2(s1,kurs1):
    return s1*kurs1
    
print('''Menu
grn - dollar--->d
dol- grn-->g''')

answer=input("Enter d or g")

if answer=="d":
    grn=int(input("Write sum grn"))
    
    print(convert(grn,27.2))
    
elif answer=="g":
    grn=int(input("Write sum grn"))
    
    print(convert2(grn,27.2))


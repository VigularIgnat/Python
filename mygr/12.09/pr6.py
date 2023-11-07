
aliens=[]
alien1={}
number_of_aliens=2


for i in range(2):
    for element in range(3):
        key=input("enter key")
        value=input("enter value")
        alien1[key]=value
    new_alien=alien1
    aliens.append(new_alien)
h=1   
for alien in aliens:
    print(f"check data about {h} alien{aliens}")
    h=h+1

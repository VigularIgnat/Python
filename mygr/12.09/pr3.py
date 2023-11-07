alien={}
keys=["age","name", "color"]

print("Choose values for this Keys")

for i in keys:
    print(i.title())
    value=input("enter value")
    alien[i]=value
    
print("Check your data")

for key,value in alien.items():
    print(key,"-", value)

speed=["fast","medium", "slow"]

print()
print("Choose your speed")

for elem in speed:
    print(elem.title(), end=" ")

speed_chosen=input("Enter value")

alien['speed']=speed_chosen
speed_chosen=speed_chosen.lower()


print()

print(alien)

if speed_chosen=="slow":
    x_increment=1
    print("Your speed increment=",x_increment)
    
elif speed_chosen=="medium":
    x_increment=2
    print("Your speed increment=",x_increment)
elif speed_chosen=="fast":
    x_increment=3
    print("Your speed increment=",x_increment)

    
alien['x.increment']=x_increment

print(alien)

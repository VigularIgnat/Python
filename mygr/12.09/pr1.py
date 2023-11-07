alien={
    "name":"artem",
    "age":34,
    "color":"blue"
    
    }

#print dictionary
for key, value in alien.items():
    print(key, " ",value)
    
#add element to dictionary
for i in range(3):
    key=input("enter key of dictionary ")
    value=input("enter value of dictionary")
    alien[key]=value


#select element in dictionary
    
print(alien["name"].title())


    

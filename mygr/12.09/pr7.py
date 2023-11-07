order=[]
ingredients={}

#2-number of order

for i in range(2):
    name_off_order=input("Enter name of order")
    for elem in range(3):#3 ingredients in order
        key=input("Enter name of engredients")#name of ingredient
        value=input("Enter number of this ingredients")#number of ingredient       
        ingredients[key]=value#add element in dictionary=ingredients
    name_order=ingredients#create element in list order 
    order.append(name_order)#add element in list order
    for i in order:#print element in list order
        print(f"{name_off_order}:{i}")
        
    
    
        

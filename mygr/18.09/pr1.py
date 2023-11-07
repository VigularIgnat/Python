orders=[]


for i in range(2):
    order={}
    print(f"Write ingredients and quentity for {i+1} order")
    for j in range(2):
        
        key=input("Enter igredients")
        value=input("Enter quentity of ingredients")
        order[key]=value
    

    orders.append(order)
print("-"*5,"check information about  order","-"*5)
r=0
for i in orders:
    r=r+1
    print(f"order{r}")
    for k,v in i.items():
        
        print(f"\t{k}-{v}")
        
    
    

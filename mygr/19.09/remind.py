order=[]
summ=0
print("="*5,"Restorant","="*5)
menu={"fish":120,
      "pizza":180,
      "fruits":50,
      "juice":40,
      "soup":160}

for key,values in menu.items():
    print(f"{key}-{values}")
while True:

    dish=input("Write dish")

    
    
    
    if dish.lower()=="end":
        break
    
    else:
        order.append(dish)
        if "fish" in order:
            summ=summ+120
            
        if "pizza" in order:
            summ=summ+180
            
        if "fruits" in order:
            summ=summ+50
            
        if "juice" in order:
            summ=summ+40
            
        if "soup" in order:
            summ=summ+160
        
for i in order:
    print(i)
    
print(f"your price {summ}")

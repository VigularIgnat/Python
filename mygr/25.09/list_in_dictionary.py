#dictionary
print("="*5+"Shop"+"="*5)

order={}
while True:
    
    anwer=input("Do your want to make order (yes or no)")
    if anwer.lower()=="yes":
        #add element in list
        shop=[]
        key=input("Enter your male")
        while True:
            
            print("if you want to stop eneter please name")
            value=input("Enetr kind of clothes")
            if value.lower()=="end":
                break
            else:
                shop.append(value)
        
        order[key]=shop
    else:
        for k,v in order.items():
            
            print(f"your ordered for {k}")
            for i in v:
                print(f"\t{i}")
               
            print(f"your order {len(shop)} things")
        break


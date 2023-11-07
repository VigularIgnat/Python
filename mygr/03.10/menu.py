
menu=[]
order={}
def Sandwich():
    while True:
        ans=input("Write do you want stop")
        eatanswer=input("Writ ename of dish")
        if ans.lower()=="end":
            for key,value in order.items():
                print(f"you order {key}:")
                for elem in value:
                    print(f"\t{elem}")
            break
        else:
            while True:
                print("If your want to stop write end")
                ingredients=input("Write ingredients")
                if ingredients=="end":
                    break
                else:  
                    menu.append(ingredients)
                     
        order[eatanswer]=menu
   
Sandwich()

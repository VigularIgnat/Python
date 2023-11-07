#dictionary
products={}
password= 3901

passwords={
    "for_enter": 3901
    }

functions=["add","delete","clear","kids","woman","mans"]



print("="*5+"Shop"+"="*5)

order={}

def add():
    while True:
        thing_for_type=[]
        enter_type=input("Enter type or not")
        
            
        if enter_type == functions[i+3] or enter_type == fucntions[-1]:
            current_type=enter_type
            while True:
                things=input("Enter name of thing")
                if things.lower()== "end":
                    break
                else:
                    thing_for_type.append(things)
                        
            products[current_type]=thing_for_type
            for k, v in products.items():
                print(f"your ordered for {k}")
                for i in v:
                    print(f"\t{i}")  
                    print(f"your add {len(thing_for_type)} things")


def function_2():
    code_delete= input("If u know password")

def  function_3():
    print(ok)

def setup():
    while True:
        print("hello")
        answer_admin=input("Enter code")
        for i in range(len(functions)-3):
            if answer_admin== functions[0]:
                add()
            elif answer_admin == functions[1]:
                function_2()
            elif answer_admin==fucntions[2]:
                function_3()
                            
                                
            else:
                print("sorry, u need to choose")
                break
def main():
    while True:
        
        answer=input("Do your want to make order (yes or no)")
        if answer.lower()=="yes":
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
        elif answer.lower()== "admin":
            admin=int(input("write password"))
            if admin== passwords["for_enter"]:
                setup()
                break
        else:
            for k,v in order.items():
                
                print(f"your ordered for {k}")
                for i in v:
                    print(f"\t{i}")
                   
                print(f"your order {len(shop)} things")
            break


main()




            





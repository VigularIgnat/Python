animals={"name":"bob",
         "eat":["meat","milk","meat","fish"]}

our_person={"name":"Jack",
            "contacts":["2309090","2039090","4344900"]}

list1=[animals,our_person]

list2=["animals","our person"]
num=0

for i in list1:
    print(f"Information about {list2[num]}")
    num+=1
    
    for key, value in i.items():
        print(key)
        if type(value)==str:
            value=value.title()
            print(f"{value}")
        else:
            num2=1
            for elem in value:
                print(f"{elem}-{num2}", end=",")
                num2=num2+1
        
    

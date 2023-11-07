while True:
    first=input("Write two mun")
    second=input("Write second")
    if first or second=="exit":
        break
    first=int(first)
    second=int(second)   
    print(first/second)
    print("You can not divide by zero")
            

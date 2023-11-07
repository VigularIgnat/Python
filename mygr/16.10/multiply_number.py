n=int(input("Write number"))

d=1
number=n
while True:
    if number==0:
        
        break
    
    d=d*number%10
    
    number=number//10    
    
print(d)

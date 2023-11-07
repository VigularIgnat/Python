grn=int(input("Write quantity"))
month=int(input("input qualitity of mounth"))
rate=int(input("input rate"))


for i in range(month):
    grn=grn+(grn*rate/100)
    
         
print(grn) 

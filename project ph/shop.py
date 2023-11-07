print(''' 1-milk)
2-tea
3-bread
4-candies''')
s=0
number_product=int(input("input number of product"))
for i in range(number_product):
    cod_product=input("input kod")
    if cod_product=='1':
        s+=27
    elif cod_product=='2':
        s+=20
    elif cod_product=='3':
        s+=35
    elif cod_product=='4':
        s+=100
print("you must pay %s grn"%(s))

name=[["2016 ","2017 ","2018"],["Dnipro","Shaschtar","Dnipro"]]
conunt=0
for row in name:
    for elem in row:
        print(elem, end=" ")
        if elem=="Dnipro":
            conunt+=1
    print()
    
print(conunt)

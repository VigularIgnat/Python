#багатовимірні списки
list1=[
    [1,2,4],
    ["file","bit","byte"],
    [4,"g",5]
    
    ]
for i in list1:
    print(i)
   

    
print(list1[1][0])

for row in list1:
    for elem in row:
        if elem=="file":
            print("file")


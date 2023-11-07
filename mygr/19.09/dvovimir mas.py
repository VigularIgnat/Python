mas=[[1,3,6,8],[2,4,6,7],[2,4,6,8],[0,2]]
#print(mas)
#variant 1
summ=0
for row in mas:
    for elem in row:
        print(elem, end=" ")
    print()


for row in mas:
    sumrow=0
    for elem in row:
        summ=summ+elem
        sumrow=sumrow+elem
    print(sumrow )
    
        

    



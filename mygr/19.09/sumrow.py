mas=[[1,3,6,8],[2,4,6,7],[2,4,6,8],[0,2]]
#print(mas)
#variant 1
summ=0
for row in mas:
    for elem in row:
        print(elem, end=" ")
    print()

num=0
minn=2147483647
numberrow=1
for row in mas:
    sumrow=0
    
    for elem in row:
        summ=summ+elem
        sumrow=sumrow+elem
    if sumrow<minn:
        minn=sumrow
        
    else:
        numberrow+=1
    print(f"sum row {num}=",sumrow )
    num=num+1
    
print(minn,numberrow)

    
        


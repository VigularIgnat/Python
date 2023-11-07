mas=[[1,3,6,8],[2,4,6,7],[2,4,6,8],[0,2]]
summ=0
num=0
minn=2147483647
for row in mas:
    sumrow=0
    minn=2147483647
    for elem in row:
        summ=summ+elem
        sumrow=sumrow+elem
    if sumrow<minn:
        minn=sumrow
    print(f"sum row {num}=",sumrow )
    num=num+1
    
print(minn)

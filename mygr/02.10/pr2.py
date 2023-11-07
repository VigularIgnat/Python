mas=[[2,3,4,5,6,6],[3,4,5,6,9,9]]
num=1
for row in mas:
    
    for elem in row:
        print(elem, end=' ')
        
    print(f"max in row {num} {max(row)}")
    
    print(f"sum in row {num} {sum(row)}")
    print(f"min in row {num} {min(row)}")

    print(f"num of max  in  {num} {row.count(max(row))}")
    num+=1
    

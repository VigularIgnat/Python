import random
num=random.randint(100,1000)

num=list(str(num))

print(num)

for i in num:
    i=int(i)
    print(i)
    
num.sort(reverse=True)



num=str(num)
print(num)
s=""
for i in num:
    s=s+i
    
print(s)
    

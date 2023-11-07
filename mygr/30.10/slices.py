import random

n=[]
for i in range(random.randint(10,20)):
    e=random.randint(1,10)
    n.append(e)
print(n)

print(max(n[0:5]))

print(n[0::2])


print(n[::-1])

import random
n=random.randint(100,1000)
print(n)
n3=n//100
n2=n//10%10
n1=n%10
print(n1, n2,n3)

number=str(max(n1,n2,n3))+str(sum([n1,n2,n3])-(max(n1,n2,n3)+min(n1,n2,n3)))+str(min(n1,n2,n3))
print(number)

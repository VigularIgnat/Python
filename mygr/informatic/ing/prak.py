a=int(input("Введіть число "))
s=0
x=a
while x>0:
    k=x%10
    s=s+k
    x=x//10
print("Сума цифр =",s)

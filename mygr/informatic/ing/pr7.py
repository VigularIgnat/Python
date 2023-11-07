s=input("Введіть речення ")
k=1
n=len(s)
for i in range(n):
    l=s[i]
    if l==" ":
        k=k+1
print("Кількість слів у реченні",k)

s=input("Enter string")
first=0
end=-1
k=0

for i in range(len(s)//2):
    if (s[first]==s[end]):
        k+=1
        end-=1
        first+=1
        print(k,first,end)
if (k==len(s)//2):
            print("Its pal")
else:
    print("is not pal")

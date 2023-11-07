s= 1000
p=10
n=0
while True:
    
    s=s+(s*p)/100
    n=n+1
    if s>=10000:
        break

    
print(n)

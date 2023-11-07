import random
n=random.randint(1,1000)
print(n)
#sum nubers
s=0
while True:
    if n//10==0:
        s=s+n
        break
    s=s+n%10
    n=n//10
    print(n)
    
print(s)

#set-множина

list1=[4,5,6,7,4,5,4,5]
print(set(list1))

word=input("Enter word")
word=list(word)
print(len(set(word)))



name="Hello"
surname="World"
a3=name+" "+surname

s1="0123456789"

r2=s1[7:9]
print(r2)

s=str(input("Enter string: "))

for c in s:
    print(c)

g="I like to travel"

count=0
for c in g:
    if c==" ":
        count=count+1
print(count)

r1=input("write sentence")
r2=input("write sentence")

if r1>r2:
    print("r1 more")
elif r2>r1:
    print("r2 more")
else:
    print("r2=r1")
a='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ut lacus quis risus dictum molestie non a
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ut lacus quis risus dictum molestie non ac turpis.'''
t=0
for c in a:
    if c==",":
        t=t+1
print(t)

txt="Lorem ipsum dolor sit amet"
print("amet" in txt)

if "amet" in txt:
    print("yes, its present")

txt="Lorem ipsum dolor sit amet"
print("ty" not in txt)

a="Hello word"
print(a.upper())#робить все великими

print(a.lower())#робить все маленькими

a="  Hello world  "
print(a.strip())#видаляє пропуски

a="TTTyppoo"
print(a.replace("T", ","))

a="Hello, World  "
print(a.split(","))



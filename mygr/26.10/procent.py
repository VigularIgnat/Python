i=0
h=0
s=10
while True:
    i=i+1
    h=h+s
    s=s-s*0.1
    print(s,h)
    if h>=50:
        break


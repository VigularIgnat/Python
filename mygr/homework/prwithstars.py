star="*"
enter=" "

for i in range(3):
    num=0
    for j in range(3):
        print(enter*(3-num), star*(1+num), enter*(3-num), end=" ")
    num=num-1
    print()

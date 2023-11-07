S=int(input("Сума вкладу = "))
k=int(input("Відсоток річних = "))
Sp=0
for i in range(4):
    i=i+1
    p=S*k/100
    print("За ",i, "рік", p)
    S=S+p
    Sp=Sp+p
print("Загальна сума прибутку",Sp,"грн")

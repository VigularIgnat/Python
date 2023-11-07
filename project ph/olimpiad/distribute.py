boy=int(input("Enter number of boy"))
girls=int(input("Enter number of girls"))

k=int(input("Enter number"))

summ_girls=girls//k

if girls%k>0:
    summ_girls+=1


print(summ_girls)

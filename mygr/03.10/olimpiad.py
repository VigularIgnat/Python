import random
mas=[]
inf=1,9223372036854775806
rand_num=random.randint(10,70)
for i in range(5):
    number=random.randint(1,10)
    
    mas.append(number)

print(mas)
count_max_elem=mas.count(max(mas))
summ_mas=sum(mas)
max_element=max(mas)
rez=summ_mas-count_max_elem*max_element
print(rez)



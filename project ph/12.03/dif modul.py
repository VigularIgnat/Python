from math import *
def func_sqrt(n):
    print(sqrt(n))
def func_sum(n):
    s=0
    for i in range(n+1):
        s=s+i
    return s
def func_factoral(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("input number"))
print('''
Menu:
sqrt-корінь;
summ-сумма;
fact-факторіал;
exit-вихіт''')
running=True
while running==True:
    answer=input("write answer")
    if answer== "sqrt":
        func_sqrt(n)
    elif answer=="summ":
        print(func_sum(n))
    elif answer=="fact":
        print(func_factoral(n))
    else:
        running=False

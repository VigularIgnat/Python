import random
compliments=["you are the pretiest","you are the best","you are the greatiest"]
print("generator of compliments")
running=True
print('''
menu:
c-Play
q-Quit''')

while running==True:
    answer=input("Choose a letter")
    if answer =="c":
        print(random.choice(compliments))
    if answer =="q":
        running==False

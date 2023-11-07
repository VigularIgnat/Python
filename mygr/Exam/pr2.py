print("You in cinema.Please enter your age ")
while True:
    print("If you want to stop write end")
    answer=input("Write your age")
    if answer.lower()=="end":
        break
    else:
        answer=int(answer)
        if answer<=3:
            print("For you we haven't cost")
        elif answer<12>3:
            print("You may buy for 10$")
        elif answer>=12:
            print("Cost of ticket 15$")

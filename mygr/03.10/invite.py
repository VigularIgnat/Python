invite_people=["ivan","maria","artem","sasha"]

def add():
    for i in range(3):
        invite=input("Write name of person")
        while invite=='end':
            for elem in invite_people:
                if invite.lower==elem:
                    print(f"This person {invite}.title() in list")
                else:
                    invite_people.append(invite)
            
add()

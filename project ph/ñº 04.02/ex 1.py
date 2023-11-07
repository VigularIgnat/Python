print("season")
def season(mounth):
    if (mounth==12) or (mounth==1) or (mounth==2):
        print("winter")
    if (mounth==3) or (mounth==4) or (mounth==5):
        print("spring")
    if (mounth==6) or (mounth==7) or (mounth==8):
        print("summer")
    if (mounth==9) or (mounth==10) or (mounth==11):
        print("autumn")
mounth=int(input("write number of mounce"))
season(mounth)

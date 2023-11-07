star="*"
enter=" "
number=int(input("number eneter"))
star_number=1
enter_number=number-1
for i in range(number):
    print(enter*enter_number+star*star_number)
    
    star_number+=2
    enter_number-=1

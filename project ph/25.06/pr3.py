try:
    print(x)
except:
    print("an exeption occured")

try:
    print(x)
except NameError:
    print("Vauiable is not defined")
except:
    print("somesing other")

try:
    print("Hello")
except:
    print("something when wrong")
else:
    print("nothing went wrong")
    
#https://www.w3schools.com/python/python_try_except.asp

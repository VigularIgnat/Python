def myfunc1(n):
    return lambda a: a * n
mydobler = myfunc1(2)
print(mydobler(11))

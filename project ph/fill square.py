import turtle
t= turtle.Pen()
t.color(1,0,0)
def my_square(site, siteb, fill):
    if fill== True:
        t.begin_fill()
    for x in range(1,3):
        t.forward(site)
        t.left(90)
        t.forward(siteb)
        t.left(90)
    if fill== True:
        t.end_fill()
        
my_square(150,50,True)

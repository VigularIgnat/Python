#програма оцінки
#вхідні дані: оцінка grade
#вихідні дані: рівень, до якого належить оцінка
#Костенко Іван, 7г

grade=int(input("Введіть оцінку "))
if grade >= 1 and grade <=3:
    print("початковий рівень")
elif grade >=4 and grade <= 6:
    print("середній рівень")
elif grade >=7 and grade <= 9:
    print("достатній рівень")
elif grade >=10 and grade <= 12:
    print("високий рівень")
else:
    print("необхіодно ввести оцінку від 1 до 12")
    
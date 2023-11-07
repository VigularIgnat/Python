persons={
    "Artem":[4,90],
    "Fedor":[50,120],
    "Annn":[60,66],
    "Lilly":[7,13],
    "Max":[5,17]
}

for key, value in persons.items():
    print(f"{key}'s favourite numbers is:")
    for elem in value:
        print(f"{elem}", end=" ")
    print()

alien={
    "name":"artem",
    "age":34,
    "color":"blue"
    
    }

print("Choose informations about alien")

for key in sorted(alien.keys()):
    print(key)

    
key1=input("enter key of information")


print(alien[key1].title())

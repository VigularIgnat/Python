#list in dictionary
pizza={"name":"firmova",
       "toppings":["mushrooms","extracheese"]
    }

print(f'''Your ordered:
{pizza["name"]}- name pizza
with the following toppings:''')

for i in pizza["toppings"]:
    print("\t"+i)

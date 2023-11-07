users={
    "phone":"Samsung s9",
    "surname":"Vigulyar",
    "email":"ignt@gmail.com"

}


for key in users:
    print(key, "-", users[key])

for key, value in users.items():
    print(key, "-", value)

key_users=input("Enter key of dictionary")
item_users=input("Enter item of dictionary")
users[key_users]=item_users

for key, value in users.items():
    print(key, "-", value)
    
users.pop("phone")

users.update({"skype":"mustang",
              "team":"Pcg"})
print(users)


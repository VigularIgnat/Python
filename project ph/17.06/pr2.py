users={
    "Tom": {
        "phone":"0991976717",
        "email":"tom@gmail.com"
        },
    "Bob":{
        "phone":"90900909",
        "email":"bob@gmail.com",
        "skype":"bob1"
        }

    }
old_email=users["Tom"]["email"]
users["Tom"]["email"]="super@gmail.com"

key="skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")
if key in users["Bob"]:
    print(users["Bob"]["skype"])
key_users=input("write key")
item_users=input("write item")
users["Bob"][item_users]=key_users

print(users)



# dictionarity in dictionarity
users={
    "aenshtein":{
            "first":"albert",
            "last":"enshtein",
            "location":"printeon",
            "gmail":"aenshtein@gmail.com"
            },
    "mcurie":{
        "first":"maria",
        "last":"curie",
        "location":"paris",
        "gmail":"mcurie@gmail.com"
        },
    "artbuk":{
        "first":"artem",
        "last":"bucksin",
        "location":"Oslo",
        "gmail":"bucks@gmail.com"
        }
    }
print(f"our site visit:")
for usernick, userinfo in users.items():
    print(f"\nUser:{usernick}")
    full_name=f"{userinfo['first'].title()} {userinfo['last'].title()}"
    print(f"\t Full name user {full_name}")
    print()
    print(f"Gmail of {usernick} is {userinfo['gmail'].title()}")






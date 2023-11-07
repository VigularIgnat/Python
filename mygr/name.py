friends=["sasha", "oleg", "nas"]
num=len(friends)
for friend in friends:
    print(friend.title())
    if friend=="oleg":
        print(f"it is a very facinating name={friend.upper()}")
print(num)

print(f"i am so sorry {friends[-1].title()}")

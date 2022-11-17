import json
with open("users.json") as users:
    data = json.load(users)
    for x in range(4):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
import json

with open("LeerJSON/note.json") as file:
    data=json.load(file)

print(data)
print(data["clientesA"])
print(data["clientesB"])
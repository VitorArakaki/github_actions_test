import json

file = open(r'teste.json')

file_json = json.load(file)


name = "teste novo 4"

value = "teste action novo 4 new"

verify = False
emp = False

new_json = []

if len(file_json["records"]) > 0:
    for r in file_json["records"]:
        if name == r["name"]:
            verify = True
            new_j = {"name": name, "value": value}
            new_json.append(new_j)
        else:
            new_json.append(r)
else:
    print("empty")

if emp == True or verify == False:
    file_json["records"].append({"name": name, "value": value})
else:
    file_json["records"] = new_json

with open("teste.json", "w") as new_file:
    json.dump(file_json, new_file)

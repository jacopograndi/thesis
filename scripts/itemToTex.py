import json

with open("items.json", "r") as f: j = json.loads(f.read())

for item in j["items"]:
    line = str(item["name"])+" & "
    line += str(item["fragility"])+" & "
    line += str(item["weight"])+"\\\\"
    print(line)

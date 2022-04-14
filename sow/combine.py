import json

with open("preparation.json") as prep:
    obj_prep = json.load(prep)

with open("ingredients.json") as ing:
    obj_ing = json.load(ing)

obj_prep.sort(key=lambda x: x["name"])
obj_ing.sort(key=lambda x: x["name"])

f = []
for i in obj_ing:
    ing_name = i["name"]
    for j in obj_prep:
        prep_name = j["name"]
        if ing_name == prep_name:
            i["preparation"] = j
            f.append(i)
            break

for reci in f:
    reci["preparation"].pop("name")

json_object = json.dumps(f, indent=4)

with open("f.json", "w") as outfile:
    outfile.write(json_object)

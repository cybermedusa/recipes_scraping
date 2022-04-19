import json

with open("preparation.json") as prep:
    obj_prep = json.load(prep)

with open("ingredients.json") as ing:
    obj_ing = json.load(ing)

obj_prep.sort(key=lambda x: x["link"])
obj_ing.sort(key=lambda x: x["link"])

f = []
for i in obj_ing:
    ing_name = i["link"]
    for j in obj_prep:
        prep_name = j["link"]
        if ing_name == prep_name:
            i["preparation"] = j
            f.append(i)
            break

for reci in f:
    reci["preparation"].pop("link")

json_object = json.dumps(f, indent=4)

with open("full_recipes.json", "w") as outfile:
    outfile.write(json_object)

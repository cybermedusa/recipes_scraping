import json

with open("full_recipes_img.json") as fri:
    obj_fri = json.load(fri)

with open("recipe_names.json") as rn:
    obj_rn = json.load(rn)

obj_fri.sort(key=lambda x: x["link"])
obj_rn.sort(key=lambda x: x["link"])

f = []
for i in obj_fri:
    fri_name = i["link"]
    for j in obj_rn:
        rn_name = j["link"]
        if fri_name == rn_name:
            i["name"] = j
            f.append(i)
            break

for reci in f:
    reci["name"].pop("link")
    reci['name'] = reci['name']['name']

json_object = json.dumps(f, indent=4)

with open("full_recipes_img_name.json", "w") as outfile:
    outfile.write(json_object)

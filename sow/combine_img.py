import json

with open("images.json") as img:
    obj_img = json.load(img)

with open("full_recipes.json") as fr:
    obj_fr = json.load(fr)

obj_img.sort(key=lambda x: x["link"])
obj_fr.sort(key=lambda x: x["link"])

f = []
for i in obj_fr:
    fr_name = i["link"]
    for j in obj_img:
        img_name = j["link"]
        if img_name == fr_name:
            i["img"] = j
            f.append(i)
            break

for reci in f:
    reci["img"].pop("link")
    reci['img'] = reci['img']['src']

json_object = json.dumps(f, indent=4)

with open("full_recipes_img.json", "w") as outfile:
    outfile.write(json_object)

from bs4 import BeautifulSoup
import itertools as it
from requests import get
import json
from links_array import p_with_h4
from functions import get_value, return_arr

recipe_p = []
recipes_p = []
dishes_preparation = []
for link in p_with_h4:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    full_content = list(filter(lambda x: x != '\n', b_s.select_one('.method-body').contents))
    # [idx for idx, val in enumerate(full_content) if val.name == "div"].pop(0)
    # [idx for idx, val in enumerate(full_content) if val.name == "h4"].pop(0)
    if full_content[0].name != 'h4':
        full_content = full_content[1:]

    full_content = full_content[:-3]
    titles = []
    for i in full_content:
        if i.name == "h4":
            titles.append(i)

    grouped = [list(grp) for match, grp in it.groupby(full_content, lambda condition: condition.name == "p") if match]

    final = [sub[item] for item in range(len(grouped)) for sub in [titles, grouped]]

    for x in range(0, len(final), 2):
        title = final[x]
        content = final[x + 1]
        sub_obj = {
            "title": '',
            "content": ''
        }
        title = final[x].get_text().strip()
        sub_obj["title"] = title
        content = [i.get_text().strip() for i in content]
        sub_obj["content"] = get_value(content)
        recipe_p.append(sub_obj)
    recipes_p.append(recipe_p)
    dish = {
        "name": link,
        "recipe": recipes_p
    }
    dishes_preparation.append(dish)
    recipe_p = []
    recipes_p = []

    json_object = json.dumps(dishes_preparation, indent=4)

    with open("recipes_p_with_h4.json", "w") as outfile:
        outfile.write(json_object)








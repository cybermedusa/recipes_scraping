from bs4 import BeautifulSoup
import itertools as it
from requests import get
import json
from links_array import p_with_h4
from functions import get_value

recipe_p = []
recipes_p = []
dishes_prep_p = []
for link in p_with_h4:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    full_content = list(filter(lambda x: x.next.name != "hr" and x != "\n" and x != "hr" and x.name != "hr", b_s.select_one(".method-body").contents))

    first_idx = [idx for idx, val in enumerate(full_content) if val.name == "h4"].pop(0)
    last_idx = [idx for idx, val in enumerate(full_content) if val.name == "div"].pop(0)
    full_content = full_content[first_idx:last_idx]

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
    # recipes_p.append(recipe_p)
    dish = {
        "link": link,
        "recipe": recipe_p
    }
    dishes_prep_p.append(dish)
    recipe_p = []
    # recipes_p = []

    json_object = json.dumps(dishes_prep_p, indent=4)

    with open("preparation_p.json", "w") as outfile:
        outfile.write(json_object)

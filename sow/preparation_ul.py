from bs4 import BeautifulSoup
from requests import get
import json
from links_array import ul_links
from functions import get_value

recipe_ul = []
recipes_ul = []
dishes_prep_ul = []
for link in ul_links:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    full_content = list(filter(lambda x: x != '\n', b_s.select_one('.method-body').contents))
    clean_content = list(filter(lambda x: x.name == 'h4' or x.name == 'ul', full_content))
    clean_content.insert(0, "Preparation")
    for i in range(0, len(clean_content), 2):
        title = clean_content[i]
        content = clean_content[i + 1]

        sub_obj = {
            "title": '',
            "content": ''
        }
        title = title if clean_content[i] == 'Preparation' else title.get_text()
        sub_obj['title'] = title
        content = [content.get_text().strip()]
        sub_obj['content'] = get_value(content)
        recipe_ul.append(sub_obj)
    recipes_ul.append(recipe_ul)
    dish = {
        "name": link,
        "recipe": recipes_ul
    }
    dishes_prep_ul.append(dish)
    recipe_ul = []
    recipes_ul = []

    json_object = json.dumps(dishes_prep_ul, indent=4)

    with open("preparation_ul.json", "w") as outfile:
        outfile.write(json_object)

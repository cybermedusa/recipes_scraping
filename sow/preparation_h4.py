from bs4 import BeautifulSoup
from requests import get
import json
from links_array import h4_links
from functions import get_value

recipe_h4 = []
recipes_h4 = []
dishes_prep_h4 = []
for link in h4_links:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    full_content = list(filter(lambda x: x != '\n', b_s.select_one('.method-body').contents))
    clean_content = list(filter(lambda x: x.name == 'h4' or x.name == 'ul', full_content))
    for i in range(0, len(clean_content), 2):
        title = clean_content[i]
        content = clean_content[i + 1]

        sub_obj = {
            "title": '',
            "content": ''
        }
        title = title.get_text().strip()
        sub_obj['title'] = title
        content = [content.get_text().strip()]
        sub_obj['content'] = get_value(content)
        recipe_h4.append(sub_obj)
    # recipes_h4.append(recipe_h4)
    dish = {
        "link": link,
        "recipe": recipe_h4
    }
    dishes_prep_h4.append(dish)
    recipe_h4 = []
    # recipes_h4 = []

    json_object = json.dumps(dishes_prep_h4, indent=4)

    with open("preparation_h4.json", "w") as outfile:
        outfile.write(json_object)

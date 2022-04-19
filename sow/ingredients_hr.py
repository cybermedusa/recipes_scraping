from bs4 import BeautifulSoup
from requests import get
from links_array import hr_link
import json
from functions import get_value

recipes = []
dishes = []
for link in hr_link:
    new_page = get(link)
    recipe = []
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    contents = list(filter(lambda x: x != '\n', b_s.select_one(".ingredients-body").contents))
    contents = list(filter(lambda x: x.name != "div", contents))
    x = contents
    if contents[1].next.name == "strong":
        contents = contents[1:]
    else:
        contents[0] = "Ingredients"
    for i in range(0, len(contents), 2):
        title = contents[i]
        content = contents[i + 1]

        recipe_obj = {
            "title": '',
            "content": ''
        }

        title = title if contents[i] == 'Ingredients' else title.get_text()
        recipe_obj['title'] = title
        clear_content = [j.get_text().strip() for j in list(filter(lambda x: x != '\n', content.contents))]
        recipe_obj['content'] = get_value(clear_content)
        recipe.append(recipe_obj)
    dish = {
        "link": link,
        "ingredients": recipe
    }
    recipe = []
    dishes.append(dish)

    json_object = json.dumps(dishes, indent=4)

    with open("ingredients_hr.json", "w") as outfile:
        outfile.write(json_object)
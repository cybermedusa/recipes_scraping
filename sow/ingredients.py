from bs4 import BeautifulSoup
from requests import get
from titles import links_list
import json
from functions import get_value

recipes = []
dishes = []
for link in links_list:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    recipe = []
    contents = list(filter(lambda x: x != '\n', b_s.select_one(".ingredients-body").contents))

    if len(contents) % 2 != 0:
        contents.insert(0, 'Ingredients')

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
    recipes.append(recipe)

    dish = {
        "name": link,
        "recipe": recipes
    }
    recipes = []
    dishes.append(dish)

    json_object = json.dumps(dishes, indent=4)

    with open("ingredients.json", "w") as outfile:
        outfile.write(json_object)

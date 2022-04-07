from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list, titles
import json


def get_ingredients(arr):
    ingredients = []
    for ing in arr:
        ingredients.append({
            "text": ing
        })
    return ingredients


recipes = []
dishes = []
for link in range(len(links_list)):
    new_page = get(links_list[link])
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
        recipe_obj['content'] = get_ingredients(clear_content)
        recipe.append(recipe_obj)
    recipes.append(recipe)

    dish = {
        "name": titles[link],
        "recipe": recipes
    }
    recipes = []
    dishes.append(dish)

    json_object = json.dumps(dishes, indent=4)

    with open("ingredients_half.json", "w") as outfile:
        outfile.write(json_object)

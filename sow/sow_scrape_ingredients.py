from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list
import json


def get_ingredients(arr):
    ingredients = []
    for ing in arr[:-1]:
        if '\n' in ing:
            ing = ing.replace('\n', '')
            ingredients.append({
                "text": ing
            })
        else:
            ingredients.append({
                "text": ing
            })
    return ingredients


recipes = []
recipe = []

for link in links_list[:150]:
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
        content = content.get_text().split('\n\n')
        recipe_obj['content'] = get_ingredients(content)
        recipe.append(recipe_obj)
    recipes.append(recipe)

json_object = json.dumps(recipes, indent=4)

# Writing to sample.json
with open("ingredients.json", "w") as outfile:
    outfile.write(json_object)
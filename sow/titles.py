from bs4 import BeautifulSoup
from requests import get
import json

URL = 'https://schoolofwok.co.uk/tips-and-recipes?sort=latest&filter=recipe'
page = get(URL)
url = 'https://schoolofwok.co.uk'
bs = BeautifulSoup(page.content, 'html.parser')
links_list = []
titles = []

for recipe in bs.find_all('div', class_='col-xs-6 col-md-3'):
    title = recipe.find('span', class_='title').get_text().strip()
    links = recipe.find('a')['href']
    new_links = url + links
    # titles.append(new_links)
    obj = {
        "link": new_links,
        "name": title
    }
    titles.append(obj)
    links_list.append(new_links)

json_object = json.dumps(titles, indent=4)

with open("recipe_names.json", "w") as outfile:
    outfile.write(json_object)
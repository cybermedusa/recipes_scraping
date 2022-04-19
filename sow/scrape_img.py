from bs4 import BeautifulSoup
from requests import get
from titles import links_list
import json

images = []
for link in links_list:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    x = b_s.select_one(".recipe-image").contents
    y = x[0].attrs["src"]
    img_obj = {
        "link": link,
        "src": y
    }
    images.append(img_obj)
json_object = json.dumps(images, indent=4)

with open("images.json", "w") as outfile:
    outfile.write(json_object)
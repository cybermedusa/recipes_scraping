from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list
from csv import writer

with open('sow_ingredients.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['ingredients']
    thewriter.writerow(header)

    for link in links_list:
        new_page = get(link)
        b_s = BeautifulSoup(new_page.content, 'html.parser')
        for ingredient in b_s.find_all('div', class_='ingredients-body'):
            ing_list = []
            for i in range(0, len(ingredient.contents)):

                if ingredient.contents[i].get_text().strip() != '':
                    ingredients = ingredient.contents[i].get_text().strip()
                    ingredients = ingredients.replace('\n\n', '\n')
                    ingredients = ingredients.replace(',', '\n')
                    ing_list.append(ingredients)

                else:
                    ' '.join(ing_list)

            info = ing_list
            thewriter.writerow(info)

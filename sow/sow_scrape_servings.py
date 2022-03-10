from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list
from csv import writer

with open('sow_servings.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['servings']
    thewriter.writerow(header)

    for link in links_list:
        new_page = get(link)
        b_s = BeautifulSoup(new_page.content, 'html.parser')
        for serv in b_s.find_all('div', class_="row recipe-icons"):
            if serv.find('span'):
                servings = serv.find('span').get_text().strip()
            else:
                servings = ''

        info = [servings]
        thewriter.writerow(info)

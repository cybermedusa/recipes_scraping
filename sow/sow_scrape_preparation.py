from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list
from csv import writer

with open('sow_preparation.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['preparation']
    thewriter.writerow(header)

    for link in links_list:
        new_page = get(link)
        b_s = BeautifulSoup(new_page.content, 'html.parser')
        for prep in b_s.find_all('div', class_='method-body'):
            prep_list = []
            for i in range(0, len(prep.contents)):
                if prep.contents[i].get_text().strip() != '':
                    preparation = prep.contents[i].get_text().strip()
                    preparation = preparation.replace('\n\n', ',')
                    preparation = preparation.replace('\n', ',')
                    prep_list.append(preparation)
                else:
                    ' '.join(prep_list)

            info = prep_list
            thewriter.writerow(info)

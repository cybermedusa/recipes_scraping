from bs4 import BeautifulSoup
from requests import get
from sow_scrape_titles import links_list
import json
from sow_merging import h4_links, p_links, ul_links, p_ul_links

h4 = []
p = []
ul = []
p_ul = []


def fit_scenario(link_arr):
    global h4, ul, p, p_ul

    for link in link_arr:
        new_page = get(link)
        b_s = BeautifulSoup(new_page.content, 'html.parser')
        c = list(filter(lambda x: x != '\n', b_s.select_one('.method-body').contents))
        if c[0].name == 'h4':
            h4.append(link)

        if c[0].name == 'ul':
            ul.append(link)

        if c[0].name == 'p' and c[1].name != 'ul':
            p.append(link)

        if c[0].name == 'p' and c[1].name == 'ul':
            p_ul.append(link)

    return h4, ul, p, p_ul


# x = fit_scenario(links_list)

def get_preparation(arr):
    prep_steps = []
    for prep in arr:
        prep_steps.append({
            "text": prep
        })
    return prep_steps


recipe_h4 = []
recipes_h4 = []
for link in h4_links:
    new_page = get(link)
    b_s = BeautifulSoup(new_page.content, 'html.parser')
    full_content = list(filter(lambda x: x != '\n', b_s.select_one('.method-body').contents))
    clean_content = list(filter(lambda x: x.name == 'h4' or x.name == 'ul', full_content))
    sub_obj = {
        "title": '',
        "content": ''
    }

    for i in range(len(clean_content)):

        if clean_content[i].name == 'h4':
            title = clean_content[i].get_text().strip()
            sub_obj["title"] = title

        if clean_content[i].name == 'ul':
            content = [clean_content[i].get_text().strip()]
            sub_obj["content"] = get_preparation(content)

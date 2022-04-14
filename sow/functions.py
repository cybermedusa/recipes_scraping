from bs4 import BeautifulSoup
from requests import get

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
        if c[0].ing_name == 'h4':
            h4.append(link)

        if c[0].ing_name == 'ul':
            ul.append(link)

        if c[0].ing_name == 'p' and c[1].ing_name != 'ul':
            p.append(link)

        if c[0].ing_name == 'p' and c[1].ing_name == 'ul':
            p_ul.append(link)

    return h4, ul, p, p_ul


def get_value(arr):
    val_arr = []
    for val in arr:
        val_arr.append({
            "text": val
        })
    return val_arr


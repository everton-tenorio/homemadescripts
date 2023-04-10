#! /usr/bin/python3

import requests
import pandas as pd
from bs4 import BeautifulSoup as bsp

url_goal = 'https://www.goal.com/br/not%C3%ADcias/programacao-partidas-futebol-tv-aberta-fechada-onde-assistir/1jf3cuk3yh5uz18j0s89y5od6w'
req = requests.get(url_goal)

soup = bsp(req.content, 'html.parser')
h2_date_info = soup.find_all('h2')
list_tables = soup.find_all('div', attrs={'class': 'table-container-scroll'})

for index, table_html in enumerate(list_tables):
  print(f'\n-                            {h2_date_info[index].text.upper()}')
  table_fut = pd.read_html(str(table_html))
  print(table_fut)

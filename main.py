# libraries needed
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import itertools
import pandas as pd
import random
from auxiliar_func import search_by, get_data

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
# set the filters to apply
wortimmo = search_by(transaction_type='vente', location='country-1', property_type=0, min_beds=2)
# get url
response = requests.get(wortimmo, headers=headers)
html_page = BeautifulSoup(response.text, 'html.parser')

# get dataframe and convert into xls
df = get_data(html_page,5)
df.to_excel('luxemburgo_raw.xls')

# libraries needed
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import itertools
import pandas as pd
import random
from auxiliar_func import search_by, get_data
from datetime import datetime

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
# set the filters to apply
wortimmo = search_by(transaction_type='location', location='city-577', property_type=0, radius = 2, price_max = 4500, min_beds = 2, surface_min = 30)

# get url
response = requests.get(wortimmo, headers=headers)
html_page = BeautifulSoup(response.text, 'html.parser')

# set numbers of adverts to see
num = 5 # last 5 adverts
# get date
now = datetime.now() # current date and time
num=5
date_time = now.strftime("%m_%d_%Y")

# get dataframe and convert into xls
df = get_data(html_page,num)
name_excel = str(date_time+'_'+str(num)+'Adverts.xls')
df.to_excel(name_excel)

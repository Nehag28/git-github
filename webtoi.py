import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup


source = requests.get('https://timesofindia.indiatimes.com/india/coronavirus-in-india-live-updates-indian-railways-cancelled-tickets-for-regular-trains-on-or-before-june-30/liveblog/75727710.cms').text
   
soup = BeautifulSoup(source,'lxml')
weeks = soup.find_all('span')
i = len(weeks)

print([week.get_text() for week in weeks])

        
#items = soup.find_all('a')
#print([item.get_text() for item in items])
import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.flipkart.com/'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

item_pic =[]
item_pic_element = soup.find_all(class_='K6IBc-')
for item in item_pic_element:
    item_pic.append(item.text)
print(len(item_pic))  

HEADER_names = [item.find(class_='iUmrbN').get_text() for item in item_pic_element]
short_desc = [item.find(class_='BXlZdc').get_text() for item in item_pic_element]
#price = [item.find(class_='_3o3r66').get_text() for item in item_pic_element]
#items_stuff = pd.DataFrame(
  #  {'heading': HEADER_names,
  #    'short_description' : short_desc,
   #   'price': price}
#)
#print(weather_stuff)
print(HEADER_names)
print(short_desc)
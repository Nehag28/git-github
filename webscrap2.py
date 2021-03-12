from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


source = requests.get('https://www.theweathernetwork.com/ca/weather/ontario/agincourt-north').text
   
soup = BeautifulSoup(source,'lxml')
week = soup.find(class_='obs-area').text
items = soup.find(class_='temp')
print(week)




#print([items[0].find(class_='wxRow').get_text() for item in items])
#print(period_names)
#short_desc = [item.find(class_='short-desc').get_text() for item in items]
#temp = [item.find(class_='temp').get_text() for item in items]
#weather_stuff = pd.DataFrame(
 #   {'period': period_names,
  #    'short_description' : short_desc,
   #   'temperature': temp}
#)
#print(weather_stuff)
#weather_stuff.to_csv('result.csv')
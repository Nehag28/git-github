from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

source = requests.get('https://forecast.weather.gov/MapClick.php?textField1=36.37&textField2=-119.27#.XrxXxURKjIU').text
   
soup = BeautifulSoup(source,'lxml')
week = soup.find(id ='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
weather_stuff = pd.DataFrame(
    {'period': period_names,
      'short_description' : short_desc,
      'temperature': temp}
)
print(weather_stuff)
weather_stuff.to_csv('result.csv')
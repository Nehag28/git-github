import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.bankbazaar.com/reviews.html'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

review_text =[]
review_text_elements=soup.find_all(class_='text_here review-desc-more')
for item in review_text_elements:
    review_text.append(item.text)
#print(review_text)
user_name = []
user_name_element = soup.find_all(class_='js-author-name')
for name in user_name_element:
    user_name.append(name.text)
#print(user_name)
bank_name =[]
bank_name_img = soup.find_all(class_='review-bank-title')
for bank in bank_name_img:
    bank_name.append(bank.find('img').get('alt'))    
#print(bank_name) 
final_array =[]

for text,user,bank in zip(review_text,user_name,bank_name):
    final_array.append({'Review_text':text,'User':user,'Bank_name':bank})

df = pd.DataFrame(final_array)
print(df)
df.to_csv('data.csv')


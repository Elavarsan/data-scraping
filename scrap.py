from bs4 import BeautifulSoup
import requests

html_data = requests.get(
    'https://www.flipkart.com/search?q=bag&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text
soup = BeautifulSoup(html_data, 'lxml')
tag = soup.find_all('div', class_='_2B099V')
# bag = soup.find('a', class_="IRpwTa")
# print(bag.text)
for t in tag:
    #print(tag)
   print(t.text)
# 1. AI
# 2. Shoping price
# 3. web search

# for t in tag:
#     print(t.text)

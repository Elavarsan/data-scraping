import requests
from bs4 import BeautifulSoup
import pandas as pd


url = requests.get(
    "https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid").text
soup = BeautifulSoup(url, 'lxml')
portal_link = soup.find('table', class_="table")

list_of_rows = []
for row in portal_link.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th", "td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

for item in list_of_rows:
    print(' '.join(item))

dataframe = pd.DataFrame(columns=list_of_rows, index=list_of_cells)
dataframe.to_csv("new_data.csv")





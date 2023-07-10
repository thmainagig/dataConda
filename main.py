import csv

from bs4 import BeautifulSoup
import requests
import time
import lxml
from pandas import DataFrame, read_csv

res = requests.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')
soup = BeautifulSoup(res.text, 'lxml')
row_details = soup.find_all(name='span', attrs='data-table__value')
rank =[]
bachelor=[]
early_career=[]
mid_career=[]
high_meaning=[]
i = row_details.__len__()-1

for items in row_details:
    while i >= 0:
        i -= 1
        if i % 6 == 0:
            rank.append(row_details[i].getText())
        elif i % 6 == 1:
            bachelor.append(row_details[i].getText())
        elif i % 6 == 3:
            early_career.append(row_details[i].getText())
        elif i % 6 == 4:
            mid_career.append(row_details[i].getText())
        elif i % 6 == 5:
            high_meaning.append(row_details[i].getText())

df = DataFrame({
    "Rank":rank,
    "Degree": bachelor,
    "Early Career Pay": early_career,
    "Mid Career Pay": mid_career,
    "% High Meaning": high_meaning
})

# df.to_csv('new_data.csv', index=False)
# data = read_csv('new_data.csv')
# print(data.items)
new = df.groupby('Mid Career Pay')
print(df.sort_values(by='Early Career Pay', ascending=False))
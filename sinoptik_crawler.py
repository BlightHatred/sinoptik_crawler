#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
from gather_funcs import dategather, hourgather, tempgather, condgather
import csv

#requesting page from sinoptik.bg
link = "https://www.sinoptik.bg/plovdiv-bulgaria-100728193/hourly"
page = requests.get(link)
tree = page.text

soup = bs(tree, 'html.parser')

#calling data gathering functions
hours = hourgather(soup)

temps = tempgather(soup)

date = dategather(soup)

conds = condgather(soup)

# writing data down in a CSV file and printing it in terminal
header = [f'Дата : {date}', 'Час', 'Температура', 'Състояние']
with open('/home/blight/data.csv', 'w', newline='', encoding='utf-8') as datafile:
    datawriter = csv.writer(datafile, delimiter=',', 
        quoting=csv.QUOTE_MINIMAL)
    datawriter.writerow(header)
    for i in range(12):
        data = [None, hours[i], temps[i], conds[i],]
        datawriter.writerow(data)
        print(' - '.join(data[1:4]))
  


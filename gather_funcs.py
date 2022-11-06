#!/usr/bin/env python3

#those are the functions used to gather specific time and temperature data from sinoptik.bg
def dategather(soup):
    ByHourDate = soup.find('span', 'wfByHourDate')

    date = ByHourDate.text


    return date
    
def hourgather(soup):
    ByHourHour = soup.find_all('span', 'wfByHourHour')
    
    hours = []

    index = 0

    while index < 12:
        hour = ByHourHour.pop(0)
        hours.append(hour.text)
        index += 1

    return hours

def tempgather(soup):
    ByHourTemp = soup.find_all('span', 'wfByHourTemp')
    
    temps = []

    for item in ByHourTemp:
        if ByHourTemp.index(item) <= 24 and ByHourTemp.index(item) % 2 == 1:
            temps.append(item.text)

    return temps

def condgather(soup):
    ByHourCond = soup.find_all('strong', 'wfByHourCond')

    conds = []

    for i in range(12):
        cond = ByHourCond[i].text
        cond = str(cond).strip()
        conds.append(cond)
        
    return conds

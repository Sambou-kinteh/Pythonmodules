import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.XxYccJ4zYzM')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)  #also soup.find_all(TAG e.g 'a')

week = soup.find(id = 'seven-day-forecast-container')
#print(week)

items = week.find_all(class_='tombstone-container')

#print(items[0])
'''
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())'''

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descs = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        'Periods': period_names,
        'Short Descriptions': short_descs,
        'Temperatures': temps
    })  

print(weather_stuff)
weather_stuff.to_csv('weather.csv')

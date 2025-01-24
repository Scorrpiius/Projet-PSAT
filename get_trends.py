import requests
from bs4 import BeautifulSoup

r = requests.get('https://trends24.in/france/')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find_all('a', class_='trend-link')
twitter_trends = []
for link in s :
    if  link.getText() not in twitter_trends:
        twitter_trends.append(str(link.getText()))


#Write into csv
import csv

with open('twitter_trends.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for trend in twitter_trends:
        writer.writerow([trend])

from serpapi import GoogleSearch

params = {
  "api_key": "b3cd9d45879ccda703639628b2ebae72c51db6893680755fb21b5086e54f4ead",
  "engine": "google_trends_trending_now",
  "geo": "FR",
  "hl": "fr"
}

search = GoogleSearch(params)
results = search.get_dict()

google_treands = []
for search in results['trending_searches']:
    google_trends.append(search['query'])
    

with open('google_trends.csv', 'a', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for trend in google_trends:
        writer.writerow([trend])

    
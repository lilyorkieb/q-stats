from __future__ import print_function
from bs4 import BeautifulSoup
import csv
import requests

url = 'https://qalerts.app/posts/'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

with open('q-posts.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for div in soup.find_all('div', attrs={"class": "w3-cell fontsizeClass w3-medium"}):
        url = div.a['href']
        timestamp = div.find_all('b')[1].string
        writer.writerow([timestamp, url])

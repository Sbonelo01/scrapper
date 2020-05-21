#importing libraries
import csv
import requests
from bs4 import BeautifulSoup


#collecting
page = requests.get('https://web.archive.org/web/20121007072955/https://www.nga.gov/collection/anZ1.htm')
#BeatifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#removing bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

#writting to a file
f = csv.writer(open('artist_name.csv','w'))
f.writerow(['Name', 'Link'])

#pull text from the BodyText div
artist_name_list = soup.find(class_='BodyText')
#pull text from all anchor tags
artist_name_list_items = artist_name_list.find_all('a')

#print all name with a loop
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archives.org' + artist_name.get('href')

    f.writerows([names, links])


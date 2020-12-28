import requests
from bs4 import BeautifulSoup
import csv

name_list = []
with open('pages_url.csv') as file:
    read_csv = csv.reader(file, delimiter=',')
    counter = 0
    for row in read_csv:
        if counter != 0:
            name_list.append(row[0])
        else:
            counter += 1
print(name_list)

def return_input(url):
    res = requests.get(url)
    return res.content.decode()

def scrap_page(response):
    soup = BeautifulSoup(response, "html.parser")
    return soup.select_one('span[class="_52id _50f5 _50f7"]').text[1:7]

base_url = 'https://www.facebook.com/'
like_list = []
for item in name_list:
    base_url += item
    raw_data = return_input(base_url)
    likes = scrap_page(raw_data)
    like_list.append(likes)
    base_url = 'https://www.facebook.com/'


with open('pages_url.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['FB_Page_Handles', 'Likes_Count'])
    
    for i in range(len(name_list)):
        csv_writer.writerow([name_list[i], like_list[i]])

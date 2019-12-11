import requests
from bs4 import BeautifulSoup as BS
import shutil

site = 'https://fb2-epub.ru/'

page = requests.get(site).text

soup = BS(page)

divs = soup.findAll('div', {'class' : 'allEntries'})

def find_content():
	for div in divs:
		div_name = div.find('div', {'class' : 'My'}).text
		div_author = div.find('div', {'class' : 'eMessage'}).text
		# div_text = div.find('br').text

		# print(div_name, div_author)

		# img = div.find('img')
		# img_src = img.find('img').get('a')

		# src = img_src
		# response = requests.get(src, stream = True)
		# with open(img + '.jpg', 'bw') as out_file:
		# 	shutil.copyfileobj(response.raw, out_file)
		# del response

	return

print(find_content())
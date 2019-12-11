import requests
from bs4 import BeautifulSoup as BS
import shutil

site = 'https://readbooks.me/genre/?genre=%D0%94%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D1%8B'

page = requests.get(site).text

soup = BS(page)

divs = soup.findAll('div', {'class' : 'col-lg-3 col-md-4 col-sm-6 col-xs-12'})

def find_content():
	for div in divs:
		div_name = div.find('p', {'class' : 'book_name'}).text
		div_author = div.find('p', {'class' : 'book_author'}).text
		div_text = div.find('div', {'class' : 'book_desc_div'}).text

		print(div_name, div_author, div_text)

		img = div.find('a', {'class' : 'mask'})
		img_src = img.find('img').get('a')

		src = img_src
		response = requests.get(src, stream = True)
		with open(img + '.jpg', 'bw') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response

	return

print(find_content())
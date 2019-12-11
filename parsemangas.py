from bs4 import BeautifulSoup
from threading import Thread
import requests
import time


def get_response(url):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'authority': 'mangalib.me',
        'method': 'GET',
        'path': '/boruto',
        'scheme': 'https',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.1079327140.1550150668; _ym_uid=1550150668838523892; _ym_d=1550150668; cartalyst_sentinel=eyJpdiI6InA5VUVLTnBQcGdXYnZZcW5NckFjRmc9PSIsInZhbHVlIjoidHpaZ2ZiMEdEWFRBc212WDA1YU9zT2t1cmtVZ0FHR05leVNHUTlEVkVjeXJVdm9oc2VQenNYZXcxMm1zQ2R6MyIsIm1hYyI6IjVjYTc3MWM1YzRhMGRmNTY4ZjJlNTc0YThkY2I0NmJiMDMwNDg0Y2E5ODYyNzRiN2QxNGZlZWVmNmMzOTI1MGQifQ%3D%3D; __cfduid=d471cc8dbecfdfe2b40bcc9e1288d88311551966826; _gid=GA1.2.615184832.1555103456; _ym_isad=1; _ym_wasSynced=%7B%22time%22%3A1555804720080%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; XSRF-TOKEN=eyJpdiI6ImJaODBRRURnc1pRTlpHb0k2djliNUE9PSIsInZhbHVlIjoiQUZXR2R1akhDOHpRMlFDMUliNGhJbEYrUXozWGVGaVRwTlRBMllKc3dtcStITkJSV1wvWjdjQmlRMmlMSzl3OXJTQktFXC82ZnQzRTdhbVZ2SU1LU0l4UT09IiwibWFjIjoiYzNhODc2NTk4Y2ExNWQ4M2Y4NTFhZDE4ZDBkYmMxNzRkMWQwZDcxMWYwYmNkMmJlMzg1NzI2ZWE0NjVmYjAyMSJ9; laravel_session=eyJpdiI6IkxZTG9UWEFIODlWRDRtcjBWdXJNNGc9PSIsInZhbHVlIjoiWGF3SU9GN0RYaGwrSmJzQUJzY0szTXF6dEZCWm5XQ1RyVGZiUnNhU1hVN3BaTlpqSFwvc1NETnNIV1VqQSsxakRDMlJwTjBBYndQb1wvXC81RDBYcVp5NHc9PSIsIm1hYyI6ImJlZjdiOTIyNGNmYTdhMzI0MDkwZGRhYmU1MzBjZTkwYjBiODUxNzY4NjkyZDMzZjYwMmQ4ZmVkMzBlZjVhZTkifQ%3D%3D; _ym_visorc_21237529=b; _gat_gtag_UA_27663466_6=1',
        'dnt': '1',
        'referer': 'https://mangalib.me/bookmark',
        'upgrade-insecure-requests': '1',
        }
        r = requests.get(url, headers=headers)
        #for key, value in r.request.headers.items():
        #    print(key+": "+value)
        return r

def download(url, title, directory):
    ufr = get_response(url)
    f = open(r'' + directory + title + '.zip', 'wb')
    f.write(ufr.content)
    f.close()



url = 'https://mangalib.me/boruto'#str(input('Введите url сайта: \n'))
directory = 'C:/Djano/heywey/WEBAPP/books/media/'#str(input('Введите директорию для скачивания через /: \n'))




#https://mangalib.me/toukyou-kushu
soup = BeautifulSoup(get_response(url).text, 'html.parser')

for chapter in soup.find_all('div', class_='chapter-item'):
        url_download = chapter.find('div', class_='chapter-item__actions').find('a', class_='chapter-item__icon link-default').get('href')
        title = chapter.find('div', class_='chapter-item__name').find('a', class_='link-default').get('href')[20:].replace('/', '-')
        thread = Thread(target=download, args=(url_download, title, directory))
        thread.start()
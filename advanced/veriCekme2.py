import requests

from bs4 import BeautifulSoup

url = "https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

tumkelimeler = []  #Bunu çaıştırmak şart değil

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

for kelimegruplari in soup.find_all("p"):
    print(kelimegruplari)
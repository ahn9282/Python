
import requests
from bs4 import BeautifulSoup
url = "https://www.hollys.co.kr/store/korea/korStore2.do"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

trs = soup.find_all('tr')
ths = trs[0].find_all('th')
region = ths[0].string
name = ths[1].string
address = ths[3].string
tel = ths[5].string
print(f"Region: {region}")
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Tel: {tel}")
import requests
from bs4 import BeautifulSoup

url ='https://www.bet365.com/#/AVR/B146/R^1/'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
result = soup.find('div', class_='wn-PreMatchFrequentItem ')
spa = soup.select_one('div', class_='wn-PreMatchFrequentItem ')
print(spa)
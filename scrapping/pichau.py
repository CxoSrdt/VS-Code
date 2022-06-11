
from logging import exception
import requests
from bs4 import BeautifulSoup

url ='https://www.pichau.com.br/hardware/placa-de-video'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
ultima_pagina= soup.find('button', class_='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-textPrimary MuiPaginationItem-sizeLarge').get_text().strip()

for i in range(1,int(ultima_pagina)):
        url_pag = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        placas = soup.find_all('div', class_='MuiCardContent-root jss58')

        with open ('precos_das_placas.csv', 'a', newline='', encoding='utf-8') as f:
                for placa in placas:

                        marca = placa.find('h2', class_='MuiTypography-root jss66 jss67 MuiTypography-h6').get_text().strip()

                        try:
                                preco = placa.find('div', class_='jss69').get_text().strip()
                                num_preco = preco[2:]
                                num_preco = num_preco[:-3]

                        except:
                                num_preco = '0'
                        linha = marca + ';' + num_preco + '\n'
                        print(linha)
                        f.write(linha)
        print(url_pag)

        
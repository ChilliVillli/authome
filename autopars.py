from time import sleep
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from auto_xlsm import writer
import xlsxwriter

ua = UserAgent()
headers = {'User-agent': ua.random}

def get_url():

    for num in range(1):
        url = f'https://www.che168.com/china/changan/a0_0msdgscncgpi1ltocsp1exx0/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  #html.parser
        auto = soup.find_all('li', class_='cards-li list-photo-li')

        for card in auto:
            # row += 1
            dealerid = card['dealerid']
            infoid = card['infoid']
            carname = card['carname']
            price = card['price']
            photo = f"https:{card.find('img').get('src')}"
            url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'

            # page.write(f'P{row + 1}', url_work)
            # page.write(f'B{row + 1}', carname)
            # page.write(f'R{row + 1}', price)
            # page.write(f'Q{row + 1}', photo)

            yield url_work


def array():
    for url_work in get_url():

        response = requests.get(url_work, headers=headers)
        card_soup = BeautifulSoup(response.text, 'lxml')  #html.parser
        auto_card = card_soup.find_all('ul', class_='basic-item-ul')

        for j in auto_card:
            # row += 1
            for q in range(len(j.find_all('li')) - 1):

                a = j.find_all('li')[q].text
                sleep(1)

            yield a








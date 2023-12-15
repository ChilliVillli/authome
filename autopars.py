from time import sleep
import requests
import os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import xlsxwriter

ua = UserAgent()
headers = {'User-agent': ua.random}

def get_url():

    for num in range(1):
        url = f'https://www.che168.com/china/changan/a0_0msdgscncgpi1ltocsp{num}exx0/'
        # session = requests.Session()
        # session.headers.update(headers)
        # r = session.get(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  #html.parser
        auto = soup.find_all('li', class_='cards-li list-photo-li')
        # book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto.xlsx")
        # page = book.add_worksheet('авто')

        for card in auto:
            dealerid = card['dealerid']
            infoid = card['infoid']
            carname = card['carname']
            price = card['price']
            photo = f"https:{card.find('img').get('src')}"
            url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'

            yield url_work
# row = 0
# column = 2
#
#
# page.write('A1', 'Бренд')
# page.write('B1', 'Название')
# page.write('C1', 'Время листинга')
# page.write('D1', 'Отображение пробега')
# page.write('E1', 'Коробка передач')
# page.write('F1', 'Стандарты выбросов')
# page.write('G1', 'Смещение')
# page.write('H1', 'Ежегодный осмотр')
# page.write('I1', 'Cрок действия страховки истекает')
# page.write('J1', 'Гарантия истекла')
# page.write('K1', 'Обслуживание')
# page.write('L1', 'Двигатель')
# page.write('M1', 'Класс автомобиля')
# page.write('N1', 'Цвет машины')
# page.write('O1', 'Марка топлива')
# page.write('P1', 'Ссылка')
# page.write('Q1', 'Фото')
# page.write('R1', 'Цена')

def array():
    for url_work in get_url():
# for i in auto:

        count = 0
        column = 2
        # dealerid = i['dealerid']
        # infoid = i['infoid']
        # carname = i['carname']
        # price = i['price']
        # url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'
        # sleep(1)
        # response = session.get(url_work)
        response = requests.get(url_work, headers=headers)
        card_soup = BeautifulSoup(response.text, 'lxml')  #html.parser
        auto_card = card_soup.find_all('ul', class_='basic-item-ul')

    # photo = f"https:{i.find('img').get('src')}"
    # row += 1
    # page.write(f'P{row + 1}', url_work)
    # page.write(f'B{row + 1}', carname)
    # page.write(f'R{row + 1}', price)
    # page.write(f'Q{row + 1}', photo)

#     if row == 20:
#         book.close()
#         print("finish")
#         break
#
        for j in auto_card:

            for q in range(len(j.find_all('li')) - 2):

                a = j.find_all('li')[q].text
                sleep(1)
                # page.write(row, column + count, a)
                yield a
                print(a)
                count += 1


# book.close()
# print("finish")






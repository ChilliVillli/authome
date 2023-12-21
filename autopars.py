from time import sleep
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import xlsxwriter


ua = UserAgent()
headers = {'User-agent': ua.random}


url = 'https://www.che168.com/china/hafu/hafuh7/a0_0msdgscncgpi1ltocsp1exx0/'
response_page = requests.get(url, headers=headers)
soup_page = BeautifulSoup(response_page.text, 'lxml')  #html.parser
pagination = soup_page.find('div', {'id' :'listpagination'}).find_all('a')
pag = int(pagination[-2].text) + 1

book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto.xlsx")
page = book.add_worksheet('hafuh7')


row = 1
column = 2


page.write('A1', 'Бренд')
page.write('B1', 'Название')
page.write('C1', 'Год выпуска')
page.write('D1', 'Пробег')
page.write('E1', 'Коробка передач')
page.write('F1', 'Запас хода на электричестве')
page.write('G1', 'Объем двигателя (л)')
page.write('H1', 'Город нахождения')
page.write('I1', 'Привод')
page.write('J1', 'Емкость батареи')
page.write('K1', 'Тип топлива')
page.write('L1', 'Двигатель')
page.write('M1', 'Класс автомобиля')
page.write('N1', 'Цвет машины')
page.write('O1', 'Марка топлива')
page.write('P1', 'Ссылка')
page.write('Q1', 'Фото')
page.write('R1','Фото остальное')
page.write('S1', 'Цена')





def get_url():

    for num in range(1, pag):

        url = f'https://www.che168.com/china/hafu/hafuh7/a0_0msdgscncgpi1ltocsp{num}exx0/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')  #html.parser
        auto = soup.find_all('li', class_='cards-li list-photo-li')

        for _ in range(len(auto)):

            for card in auto:

                try:
                    dealerid = card['dealerid']
                    # sleep(1)
                    infoid = card['infoid']
                    carname = card['carname']
                    price = (float(card['price']) * float(10000.00))
                except KeyError:
                    continue



                url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'
                page.write(f'P{row + 1}', url_work)
                page.write(f'B{row + 1}', carname)
                page.write(f'S{row + 1}', price)

                yield url_work


def array():
    global row, column, page, carname, price, photo, pag

    # list_auto = ['上牌时间', '表显里程', '变  速  箱', '燃料类型', 'WLTC纯电续航里程',
    #              '排       量', '所  在  地', '发  动  机',
    #              '车辆级别', '车身颜色', '驱动方式', '标准容量', '燃油标号']

    for url_work in get_url():
        b = ''
        response = requests.get(url_work, headers=headers)
        card_soup = BeautifulSoup(response.text, 'lxml')  #html.parser


        try:
            photo_soup = BeautifulSoup(response.text, 'lxml')
            photo_first = photo_soup.find('a', class_='jiaodianphotoclick').find('img').get('src')
            # sleep(2)
            page.write(f'Q{row + 1}', f"https:{photo_first}")
            photo_car = photo_soup.find('div', class_='car-pic-list js-box-text').find_all('a')
        except AttributeError:
            continue


        for pc in photo_car:

            b += f"https:{pc.find('img').get('data-original')};"
        page.write_string(f'R{row + 1}', b)


        auto_card = card_soup.find_all('ul', class_='basic-item-ul')


        row += 1
        column = 2
        print(row)

        for j in auto_card:

            for q in range(len(j.find_all('li'))):

                a = j.find_all('li')[q].text

                if '上牌时间' in a:
                    page.write(f"C{row}", a.replace('上牌时间', ''))
                    column += 1
                    continue
                if '表显里程' in a:
                    page.write(f"D{row}", a.replace('表显里程', ''))
                    column += 1
                    continue
                if '变  速  箱' in a:
                    page.write(f"E{row}", a.replace('变  速  箱', ''))
                    column += 1
                    continue
                if '燃料类型' in a:
                    page.write(f"K{row}", a.replace('燃料类型', ''))
                    column += 1
                    continue
                if 'WLTC纯电续航里程' in a:
                    page.write(f"F{row}", a.replace('WLTC纯电续航里程', ''))
                    column += 1
                    continue
                if 'CLTC纯电续航里程' in a:
                    page.write(f"F{row}", a.replace('CLTC纯电续航里程', ''))
                    column += 1
                    continue
                if '排       量' in a:
                    page.write(f"G{row}", a.replace('排       量', ''))
                    column += 1
                    continue
                if '所  在  地' in a:
                    page.write(f"H{row}", a.replace('所  在  地', ''))
                    column += 1
                    continue
                if '发  动  机' in a:
                    page.write(f"L{row}", a.replace('发  动  机', ''))
                    column += 1
                    continue
                if '车辆级别' in a:
                    page.write(f"M{row}", a.replace('车辆级别', ''))
                    column += 1
                    continue
                if '车身颜色' in a:
                    page.write(f"N{row}", a.replace('车身颜色', ''))
                    column += 1
                    continue
                if '驱动方式' in a:
                    page.write(f"I{row}", a.replace('驱动方式', ''))
                    column += 1
                    continue
                if '标准容量' in a:
                    page.write(f"J{row}", a.replace('标准容量', ''))
                    column += 1
                    continue
                if '燃油标号' in a:
                    a = a.replace('燃油标号', '')
                    if '92号' or '95号' in a:
                        page.write(f"O{row}", a.replace('号', ''))
                        page.write(f"K{row}", 'бензин')
                    if '0号' in a:
                        page.write(f"O{row}", a.replace('号', ''))
                        page.write(f"K{row}", 'дизель')
                    column += 1
                    continue


        if row == 118:
            book.close()
            print("finish")
            break


    # book.close()
    # print("finish")


array()



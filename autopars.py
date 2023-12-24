from time import sleep
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import xlsxwriter


ua = UserAgent()
headers = {'User-agent': ua.random}
# headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

# list_auto_haval = ['hafuf7', 'hafuh6', 'hafuh9', 'hafudagou', 'hafum6',
        #              'hafuh5jingdian', 'hafuh5', 'hafuh2','hafuh6coupe', 'hafuf7x', 'hafuh3',
        #              'hafuh4', 'hafuh8', 'hafuh6s', 'hafuh6xinnengyuan', 'hafuchitu', 'hafukugou', 'hafushenshou',
        #              'hafuxiaolong', 'hafuerdaidagou', 'hafuerdaidagouxinnengyuan', 'hafuxiaolongmax' , 'hafuchulian',
        #              'hafuh1', 'hafuh2s', 'hafuf5']

# list_changan = ['benbenev', 'changanlumin', 'benben', 'benbenmini', 'changanbenbenestar', 'changancx20', 'yuexiangv5']
                #, 'yuexiangv3', 'yuexiang', 'yidong', 'changanuniv', 'changanunivzhidianidd', 'ruichengcc', 'ruichengplus',
                # 'yida', 'yidongdt', 'yidongxinnengyuan', 'changancx30', 'yidongxt', 'yuexiangv7', 'ruicheng', 'ruichengcc2',
                # 'lingxuan', 'changancs15', 'changancs35plus', 'changancs55plus', 'changancs75', 'changancs75plus', 'changancs75pluszhidianidd',
                # 'changanunit', 'changancs85coupe', 'changanunik', 'changanunikzhidianidd', 'changancs95', 'changancs75xinnengyuan',
                # 'changancs15ev', 'changancs35', 'changanxinnengyuanepro', 'changancs55', 'changanlantuozhe', 'fengjingfangche']

# list_chery = ['qiruiqq', 'qiruiqq3', 'fengyun2', 'qiruia1', 'qiruie3', 'qiyun', 'qiyun2', 'airuize5', 'airuize5gt', 'airuize5plus',
#               'airuize8', 'airuize3', 'airuize7', 'airuize7e', 'airuizegx', 'qiruia3', 'qiruia5', 'qiruie5', 'qiyun3', 'dongfangzhizi',
#               'ruihu3x', 'ruihu5x', 'oumengda', 'ruihu7', 'ruihu7plus', 'ruihu7plusxinnengyuan', 'ruihu8', 'ruihu8plus',
#               'ruihu8pluskunpenge', 'ruihu8pro', 'ruihu9', 'qiruix1', 'ruihu', 'ruihu3', 'ruihu5']

book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto.xlsx")
page = book.add_worksheet('chery')

row = 1
column = 2

page.write('A1', 'Бренд')
page.set_column("A:A", 10)
page.write('B1', 'Название')
page.set_column("B:B", 40)
page.write('C1', 'Артикул')
page.write('D1', 'Год выпуска')
page.set_column("D:D", 11)
page.write('L1', 'Пробег')
page.set_column("L:L", 10)
page.write('I1', 'Коробка передач')
page.set_column("I:I", 15)
page.write('Q1', 'Запас хода на электричестве')
page.set_column("Q:Q", 35)
page.write('G1', 'Объем двигателя (л)')
page.set_column("G:G", 20)
page.write('E1', 'Город нахождения')
page.set_column("E:E", 18)
page.write('J1', 'Привод')
page.set_column("J:J", 10)
page.write('P1', 'Емкость батареи')
page.set_column("P:P", 20)
page.write('F1', 'Тип топлива')
page.set_column("F:F", 12)
page.write('H1', 'Двигатель')
page.set_column("H:H", 15)
page.write('M1', 'Класс автомобиля')
page.set_column("M:M", 15)
page.write('K1', 'Цвет машины')
page.set_column("K:K", 15)
page.write('N1', 'Марка топлива')
page.set_column("N:N", 15)
page.write('O1', 'Поставщик')
page.set_column("O:O", 10)
page.write('R1', 'Ссылка')
page.write('S1', 'Фото')
page.write('T1', 'Фото остальное')
page.set_column("T:T", 15)
page.write('U1', 'Цена')


# for name in list_changan:

url = f"https://www.che168.com/china/qirui/airuizegx/"
response_page = requests.get(url, headers=headers) #, headers=headers
soup_page = BeautifulSoup(response_page.text, 'lxml')
check = soup_page.find_all('li', class_='cards-li list-photo-li')
print(len(check))

    # pagination = soup_page.find('div', {'id' :'listpagination'}).find_all('a')
    # pag = int(pagination[-2].text) + 1

    # count = 0
    #
    # if len(check) == 0:
    #     continue

    # book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto.xlsx")

    # page = book.add_worksheet(f'{name}')
    #
    # row = 1
    # column = 2
    #
    # page.write('A1', 'Бренд')
    # page.set_column("A:A", 10)
    # page.write('B1', 'Название')
    # page.set_column("B:B", 40)
    # page.write('C1', 'Артикул')
    # page.write('D1', 'Год выпуска')
    # page.set_column("D:D", 11)
    # page.write('L1', 'Пробег')
    # page.set_column("L:L", 10)
    # page.write('I1', 'Коробка передач')
    # page.set_column("I:I", 15)
    # page.write('Q1', 'Запас хода на электричестве')
    # page.set_column("Q:Q", 35)
    # page.write('G1', 'Объем двигателя (л)')
    # page.set_column("G:G", 20)
    # page.write('E1', 'Город нахождения')
    # page.set_column("E:E", 18)
    # page.write('J1', 'Привод')
    # page.set_column("J:J", 10)
    # page.write('P1', 'Емкость батареи')
    # page.set_column("P:P", 20)
    # page.write('F1', 'Тип топлива')
    # page.set_column("F:F", 12)
    # page.write('H1', 'Двигатель')
    # page.set_column("H:H", 15)
    # page.write('M1', 'Класс автомобиля')
    # page.set_column("M:M", 15)
    # page.write('K1', 'Цвет машины')
    # page.set_column("K:K", 15)
    # page.write('N1', 'Марка топлива')
    # page.set_column("N:N", 15)
    # page.write('O1', 'Поставщик')
    # page.set_column("O:O", 10)
    # page.write('R1', 'Ссылка')
    # page.write('S1', 'Фото')
    # page.write('T1', 'Фото остальное')
    # page.set_column("T:T", 15)
    # page.write('U1', 'Цена')

list_url = []


def get_url():

    for num in range(1, 6):

        url_cars = f'https://www.che168.com/china/qirui/airuizegx/a0_0msdgscncgpi1ltocsp{num}exx0/'
        response = requests.get(url_cars, headers=headers)
        # sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')
        auto = soup.find_all('li', class_='cards-li list-photo-li')

        for card in auto:

            try:
                dealerid = card['dealerid']
                infoid = card['infoid']
                carname = card['carname']
                price = (float(card['price']) * float(10000.00))
            except KeyError:
                continue

            url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'

            if url_work in list_url:
                continue

            list_url.append(url_work)

            page.write(f'R{row + 1}', url_work)
            page.write(f'A{row + 1}', 'Chery')
            page.write(f'B{row + 1}', carname)
            page.write(f'U{row + 1}', price)

            yield url_work


def array():
    global row, column, page, check

    for url_work in get_url():
        b = ''
        response = requests.get(url_work, headers=headers)
        sleep(1)
        card_soup = BeautifulSoup(response.text, 'lxml')

        try:
            photo_soup = BeautifulSoup(response.text, 'lxml')
            photo_first = photo_soup.find('a', class_='jiaodianphotoclick').find('img').get('src')
            # sleep(2)
            page.write(f'S{row + 1}', f"https:{photo_first}")
            photo_car = photo_soup.find('div', class_='car-pic-list js-box-text').find_all('a')
            provider = card_soup.find('div', class_='merchantCard_right').find_all('span')
            pr = provider[0].text
            page.write(f'O{row + 1}', pr.replace('                        ', ''))
        except AttributeError:
            continue


        for pc in photo_car:

            b += f"https:{pc.find('img').get('data-original')};"
        page.write_string(f'T{row + 1}', b)

        auto_card = card_soup.find_all('ul', class_='basic-item-ul')

        row += 1
        column = 2

        print(row)

        for j in auto_card:

            for q in range(len(j.find_all('li'))):

                a = j.find_all('li')[q].text

                if '上牌时间' in a:
                    """Год выпуска"""
                    a = a.replace('上牌时间', '')
                    page.write(f"D{row}", a[0:4])
                    column += 1
                    continue
                if '表显里程' in a:
                    """Пробег"""
                    page.write(f"L{row}", a.replace('表显里程', ''))
                    column += 1
                    continue
                if '变  速  箱' in a:
                    """Коробка передач"""
                    page.write(f"I{row}", a.replace('变  速  箱', ''))
                    column += 1
                    continue
                if '燃料类型' in a:
                    """Тип топлива"""
                    page.write(f"K{row}", a.replace('燃料类型', ''))
                    column += 1
                    continue
                if 'WLTC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    page.write(f"Q{row}", a.replace('WLTC纯电续航里程', ''))
                    page.write(f"F{row}", 'гибрид')
                    column += 1
                    continue
                if 'CLTC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    page.write(f"Q{row}", a.replace('CLTC纯电续航里程', ''))
                    page.write(f"F{row}", 'электродвигатель')
                    column += 1
                    continue
                if 'NEDC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    page.write(f"Q{row}", a.replace('NEDC纯电续航里程', ''))
                    page.write(f"F{row}", 'электродвигатель')
                    column += 1
                    continue
                if '排       量' in a:
                    """Объем двигателя (л)"""
                    a = a.replace('排       量', '')
                    if 'L' in a:
                        page.write(f"G{row}", a.replace('L', ''))
                    column += 1
                    continue
                if '所  在  地' in a:
                    """Город нахождения"""
                    page.write(f"E{row}", a.replace('所  在  地', ''))
                    column += 1
                    continue
                if '发  动  机' in a:
                    """Двигатель"""
                    page.write(f"H{row}", a.replace('发  动  机', ''))
                    column += 1
                    continue
                if '车辆级别' in a:
                    """Класс автомобиля"""
                    page.write(f"M{row}", a.replace('车辆级别', ''))
                    column += 1
                    continue
                if '车身颜色' in a:
                    """Цвет машины"""
                    page.write(f"K{row}", a.replace('车身颜色', ''))
                    column += 1
                    continue
                if '驱动方式' in a:
                    """Привод"""
                    page.write(f"J{row}", a.replace('驱动方式', ''))
                    column += 1
                    continue
                if '标准容量' in a:
                    """Емкость батареи"""
                    page.write(f"P{row}", a.replace('标准容量', ''))
                    column += 1
                    continue
                if '燃油标号' in a:
                    """Марка топлива, тип топлива"""
                    a = a.replace('燃油标号', '')
                    if '92号' or '95号' in a:
                        page.write(f"N{row}", a.replace('号', ''))
                        page.write(f"F{row}", 'бензин')
                    if '0号' in a:
                        page.write(f"N{row}", a.replace('号', ''))
                        page.write(f"F{row}", 'дизель')
                    column += 1
                    continue

        if row == 11 or (len(check) - 1) == row:
            # book.close()
            print("end")
            # count = 0
            break


array()

book.close()
print("finish")






from time import sleep
import requests
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import xlsxwriter
from googletrans import Translator


ua = UserAgent()
headers = {'User-agent': ua.random}
translator = Translator()


# headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}


# list_auto_haval = ['hafuf7', 'hafuh6', 'hafuh9', 'hafudagou', 'hafum6',
#                      'hafuh5jingdian', 'hafuh5', 'hafuh2','hafuh6coupe', 'hafuf7x', 'hafuh3',
#                      'hafuh4', 'hafuh8', 'hafuh6s', 'hafuh6xinnengyuan', 'hafuchitu', 'hafukugou', 'hafushenshou',
#                      'hafuxiaolong', 'hafuerdaidagou', 'hafuerdaidagouxinnengyuan', 'hafuxiaolongmax' , 'hafuchulian',
#                      'hafuh1', 'hafuh2s', 'hafuf5']

# list_changan = ['benbenev', 'changanlumin', 'benben', 'benbenmini', 'changanbenbenestar', 'changancx20', 'yuexiangv5']
#                 , 'yuexiangv3', 'yuexiang', 'yidong', 'changanuniv', 'changanunivzhidianidd', 'ruichengcc', 'ruichengplus',
#                 'yida', 'yidongdt', 'yidongxinnengyuan', 'changancx30', 'yidongxt', 'yuexiangv7', 'ruicheng', 'ruichengcc2',
#                 'lingxuan', 'changancs15', 'changancs35plus', 'changancs55plus', 'changancs75', 'changancs75plus', 'changancs75pluszhidianidd',
#                 'changanunit', 'changancs85coupe', 'changanunik', 'changanunikzhidianidd', 'changancs95', 'changancs75xinnengyuan',
#                 'changancs15ev', 'changancs35', 'changanxinnengyuanepro', 'changancs55', 'changanlantuozhe', 'fengjingfangche']

# list_chery = ['qiruiqq', 'qiruiqq3', 'fengyun2', 'qiruia1', 'qiruie3', 'qiyun', 'qiyun2', 'airuize5', 'airuize5gt', 'airuize5plus',
#               'airuize8', 'airuize3', 'airuize7', 'airuize7e', 'airuizegx', 'qiruia3', 'qiruia5', 'qiruie5', 'qiyun3', 'dongfangzhizi',
#               'ruihu3x', 'ruihu5x', 'oumengda', 'ruihu7', 'ruihu7plus', 'ruihu7plusxinnengyuan', 'ruihu8', 'ruihu8plus',
#               'ruihu8pluskunpenge', 'ruihu8pro', 'ruihu9', 'qiruix1', 'ruihu', 'ruihu3', 'ruihu5']
#
# list_geely = ['xiongmao', 'xiongmaojingdian', 'jilisc3', 'jingang', 'jingangcaifu', 'jinying', 'ziyoujian', 'binrui',
#               'dihao', 'dihaolhip', 'dihaoxinnengyuan', 'xingrui', 'xingruil', 'dihaogl', 'dihaoglxinnengyuan', 'dihaol', 'haijing',
#               'jiligc7', 'jingdiandihao', 'yuanjing', 'borui', 'boruixinnengyuan', 'jiliec8', 'jiaji', 'jiajixinnengyuan',
#               'yingluntx4', 'binyue', 'jiliicon', 'boyue', 'boyuel', 'dihaos', 'xingyuel', 'xingyuelzengchengdiandongban',
#               'yuanjingx6', 'haoyuel', 'binyuexinnengyuan', 'yuanjingx1', 'yuanjingx3', 'dihaogs', 'dihaogse', 'jiligx7',
#               'jilisx7', 'xingyue', 'xingyues', 'yuanjings1', 'haoqingsuv', 'haoyue']
#
# list_jike = ['jikex', 'jike009', 'jikex']
#
#
# list_GAC_TRUMPCHI = ['yingbao', 'chuanqiga3', 'chuanqiga3sshijie', 'chuanqiga4', 'chuanqiga6', 'chuanqiga5', 'chuanqiga5xinnengyuan',
#                      'chuanqiga8', 'chuanqim6', 'chuanqie9', 'chuanqim8', 'chuanqigs3', 'chuanqigs4', 'chuanqigs4plus', 'yingku',
#                      'chuanqigs8', 'chuanqigs4coupe', 'chuanqigs4xinnengyuan', 'chuanqigs5super', 'chuanqigs5', 'chuanqigs7']
#
# list_dongfeng = ['junfenger30', 'junfenge11k', 'shuaike', 'shuaikexinnengyuan', 'yuxuan', 'mengshi', 'palasuo', 'aoding',
#                  'mengshim50', 'yufengp16', 'ruiqi', 'ruiqi6', 'ruiqi6xinnengyuan']
#
# list_jietu = ['jietudasheng', 'jietudashengidm', 'jietulvxingzhe', 'jietux70', 'jietux70plus',
#               'jietux70m', 'jietux70s', 'jietux90', 'jietux90plus', 'jietux95', 'jietux70coupe']
#
# list_kaiyi = ['kaiyishiyue', 'kaiyic3', 'kaiyic3r', 'kaiyie3', 'kaiyix3', 'xuanjie',
#               'xuanjieproev', 'kaiyikunlun', 'kaiyiv3', 'kaiyix5']
#
# list_beijing = ['beijingbj40', 'beijingbj80', 'beijingbj90', 'beijingbj60', 'beijingbj20', 'beijingf40', 'beijingbj30']
#
# list_changcheng = ['changchengc30', 'changchengc30xinnengyuan', 'changchengc50', 'changchengm4',
#                    'fengjun5', 'fengjun7', 'jingangpao', 'pao', 'shanhaipao', 'fengjun6']
#
# list_tanke = ['tanke300', 'tanke500', 'tanke500xinnengyuan', 'tanke400xinnengyuan']
#
# list_ruilanqiche = ['ruilanqichex3pro', 'fengye80v', 'fengye30x', 'fengye60s']


list_changcheng = ['changanlumin', 'ruichengcc'] #, 'yuexiang', 'yidong', 'changanuniv', 'changanunivzhidianidd', 'ruichengcc', 'ruichengplus']



# book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto_copy.xlsx")
# page = book.add_worksheet('changan')

book_update = openpyxl.load_workbook("auto_copy.xlsx")
sheet = book_update.active


brand_url = 'hafu'
brand = 'Haval'
row = 1
column = 2
count_two = 0

# page.write('A1', 'Бренд')
# page.set_column("A:A", 10)
# page.write('B1', 'Название')
# page.set_column("B:B", 40)
# page.write('C1', 'Артикул')
# page.write('D1', 'Год выпуска')
# page.set_column("D:D", 11)
# page.write('E1', 'Город нахождения')
# page.set_column("E:E", 18)
# page.write('F1', 'Тип двигателя')
# page.set_column("F:F", 12)
# page.write('G1', 'Объем двигателя (л)')
# page.set_column("G:G", 20)
# page.write('H1', 'Двигатель')
# page.set_column("H:H", 15)
# page.write('I1', 'Мощность двигателя')
# page.set_column("I:I", 15)
# page.write('J1', 'Коробка передач')
# page.set_column("J:J", 15)
# page.write('K1', 'Привод')
# page.set_column("K:K", 10)
# page.write('L1', 'Цвет машины')
# page.set_column("L:L", 15)
# page.write('M1', 'Пробег')
# page.set_column("M:M", 10)
# page.write('N1', 'Класс автомобиля')
# page.set_column("N:N", 15)
# page.write('O1', 'Марка топлива')
# page.set_column("O:O", 15)
# page.write('P1', 'Поставщик')
# page.set_column("P:P", 10)
# page.write('Q1', 'Емкость батареи')
# page.set_column("Q:Q", 20)
# page.write('R1', 'Запас хода на электричестве')
# page.set_column("R:R", 35)
# page.write('S1', 'Ссылка')
# page.write('T1', 'Фото')
# page.write('U1', 'Фото остальное')
# page.set_column("T:T", 15)
# page.write('V1', 'Цена')
# page.write('W1', 'Поиск')


list_url = []


def get_url():
    global row

    while sheet[f"S{row+1}"].value != None:
        pr = row
        name = sheet[f"W{row + 1}"].value
        url = sheet[f"S{row+1}"].value

        driver_update = webdriver.Chrome()
        driver_update.get(url)
        soup_update = BeautifulSoup(driver_update.page_source, 'lxml')
        # tr = soup_update.find('div', class_='wrong_page').find('p').text.strip()
        # er = soup_update.find('div', class_='fail-title').text.strip()

        try:
            focus = soup_update.find('div', class_='tp-img-file pc-slide foucs-img-file').get('id')
            if focus == 'focus-1':
                row += 1
                list_url.append(url)
                continue
        except AttributeError:

        # if soup_update.find('div', class_='wrong_page').find('p').text.strip() != '非常抱歉，您访问的车辆信息不存在！'
        #    soup_update.find('div', class_='fail-title').text.strip() != '加载失败':
        #     row += 1
        #     continue


    # for name in list_changcheng:

            print(name)
            d = {2014: count_two, 2015: count_two, 2016: count_two, 2017: count_two, 2018: count_two,
                 2019: count_two, 2020: count_two, 2021: count_two, 2022: count_two, 2023: count_two, 2024: count_two}

            # for num in range(1, 2):

            # url_cars = f'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{num}exx0/?kw=wey'
            url_cars = f'https://www.che168.com/china/{brand_url}/{name}/a0_0msdgscncgpi1ltocsp1exx0/'
            driver = webdriver.Chrome()
            driver.get(url_cars)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            sleep(2) # response = requests.Session().get(url_cars, headers=headers)
            auto = soup.find_all('li', class_='cards-li list-photo-li')


            if auto == []:
                driver.get(url_cars)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                sleep(2) # response = requests.Session().get(url_cars, headers=headers)
                auto = soup.find_all('li', class_='cards-li list-photo-li')

            if auto != []:

                for card in auto:
                    if pr != row:
                        break

                    try:
                        dealerid = card['dealerid']
                        infoid = card['infoid']
                        carname = card['carname']
                        price = (float(card['price']) * float(10000.00))
                    except KeyError:
                        continue

                    year = ''.join(c if c.isdigit() else ' ' for c in carname).split()
                    year = [int(y) for y in year]
                    year = max(year)

                    url_work = f'https://www.che168.com/dealer/{dealerid}/{infoid}.html'

                    if year < 2014:
                        continue

                    else:
                        d[year] += 1

                    if d[year] >= 3:
                        continue

                    if url_work in list_url:
                        continue

                    # page.write(f'S{row + 1}', url_work)
                    sheet[f'S{row + 1}'] = url_work
                    # page.write(f'A{row + 1}', 'Changan')
                    sheet[f'A{row + 1}'] = brand.title()

                    # page.write(f'B{row + 1}', translator.translate(carname, dest='en').text)
                    model = translator.translate(carname, dest='en').text
                    if brand.title() not in model:
                        sheet[f'B{row + 1}'] = f'{brand.title()} {model}'
                    else:
                        sheet[f'B{row + 1}'] = model
                    # page.write(f'V{row + 1}', price)
                    sheet[f'V{row + 1}'] = price
                    yield url_work


def array():
    global row, column, page, count

    for url_work in get_url():
        b = ''
        driver_car = webdriver.Chrome()
        driver_car.get(url_work)
        card_soup = BeautifulSoup(driver_car.page_source, 'lxml')

        try:
            photo_soup = BeautifulSoup(driver_car.page_source, 'lxml')
            # photo_first = photo_soup.find('a', class_='jiaodianphotoclick').find('img').get('src')
            # # sleep(2)
            # # page.write(f'T{row + 1}', f"https:{photo_first}")
            # sheet[f'T{row + 1}'] = f"https:{photo_first}"
            photo_car = photo_soup.find('div', class_='car-pic-list js-box-text').find_all('a')
            provider = card_soup.find('div', class_='merchantCard_right').find_all('span')
            pr = provider[0].text
            # page.write(f'P{row + 1}', pr.replace('                        ', ''))
            sheet[f'P{row + 1}'] = pr.replace('                        ', '')
        except AttributeError:
            continue

        count = 1

        for pc in photo_car:
            sleep(1)
            if count == 1:
                sheet[f'T{row + 1}'] = f"https:{pc.find('img').get('data-original')}"
                count = 0
                continue
            b += f"https:{pc.find('img').get('data-original')};"
        # page.write_string(f'U{row + 1}', b)
        sheet[f'U{row + 1}'] = b
        auto_card = card_soup.find_all('ul', class_='basic-item-ul')

        row += 1
        column = 2
        print(row)

        list_url.append(url_work)

        for j in auto_card:

            for q in range(len(j.find_all('li'))):

                a = j.find_all('li')[q].text

                if '上牌时间' in a:
                    """Год выпуска"""
                    a = a.replace('上牌时间', '')
                    # page.write(f"D{row}", a[0:4])
                    sheet[f'D{row}'] = a[0:4]
                    column += 1
                    continue
                if '表显里程' in a:
                    """Пробег"""
                    a = a.replace('表显里程', '')
                    result = translator.translate(a, dest='ru').text
                    mileage = ''.join(c if c.isdigit() else '' for c in result).split()
                    mileage = [int(y) for y in mileage]
                    # page.write(f"M{row}", mileage[0])
                    sheet[f'M{row}'] = mileage[0]
                    column += 1
                    continue
                if '变  速  箱' in a:
                    """Коробка передач"""
                    a = a.replace('变  速  箱', '')
                    result = translator.translate(a, dest='ru').text
                    if result == 'автоматический':
                        # page.write(f"J{row}", 'АКПП')
                        sheet[f'J{row}'] = 'АКПП'
                    else:
                        # page.write(f"J{row}", 'МКПП')
                        sheet[f'J{row}'] = 'МКПП'
                    column += 1
                    continue
                if '燃料类型' in a:
                    """Тип двигателя"""
                    # page.write(f"F{row}", a.replace('燃料类型', ''))
                    sheet[f"F{row}"] = a.replace('燃料类型', '')
                    column += 1
                    continue
                if 'WLTC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    a = a.replace('WLTC纯电续航里程', '')
                    # page.write(f"R{row}", a[:-2])
                    sheet[f"R{row}"] = a[:-2]
                    # page.write(f"F{row}", 'гибрид')
                    sheet[f"F{row}"] = 'гибрид'
                    column += 1
                    continue
                if 'CLTC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    a = a.replace('CLTC纯电续航里程', '')
                    # page.write(f"R{row}", a[:-2])
                    sheet[f"R{row}"] = a[:-2]
                    # page.write(f"F{row}", 'Электродвигатель')
                    sheet[f"F{row}"] = 'Электродвигатель'
                    column += 1
                    continue
                if 'NEDC纯电续航里程' in a:
                    """Запас хода на электричестве"""
                    a = a.replace('NEDC纯电续航里程', '')
                    # page.write(f"R{row}", a[:-2])
                    sheet[f"R{row}"] = a[:-2]
                    # page.write(f"F{row}", 'Электродвигатель')
                    sheet[f"F{row}"] = 'Электродвигатель'
                    column += 1
                    continue
                if '排       量' in a:
                    """Объем двигателя (л)"""
                    a = a.replace('排       量', '')
                    if 'L' in a:
                        # page.write(f"G{row}", a.replace('L', ''))
                        sheet[f"G{row}"] = a.replace('L', '')
                    column += 1
                    continue
                if '所  在  地' in a:
                    """Город нахождения"""
                    a = a.replace('所  在  地', '')
                    result = translator.translate(a, dest='ru')
                    # page.write(f"E{row}", result.text)
                    sheet[f"E{row}"] = result.text
                    column += 1
                    continue
                if '发  动  机' in a:
                    """Двигатель"""
                    # page.write(f"H{row}", a.replace('发  动  机', ''))
                    sheet[f"H{row}"] = a.replace('发  动  机', '')
                    a = ''.join(l if l.isdigit() else ' ' for l in a).split()
                    if len(a) == 1:
                        # page.write(f"I{row}", a[0])
                        sheet[f"I{row}"] = a[0]
                    if len(a) > 1:
                        # page.write(f"I{row}", a[2])
                        sheet[f"I{row}"] = a[2]
                    else:
                        sheet[f"I{row}"] = a
                    column += 1
                    continue
                if '车辆级别' in a:
                    """Класс автомобиля"""
                    a = a.replace('车辆级别', '')
                    result = translator.translate(a, dest='en')
                    # page.write(f"N{row}", result.text)
                    sheet[f"N{row}"] = result.text
                    column += 1
                    continue
                if '车身颜色' in a:
                    """Цвет машины"""
                    a = a.replace('车身颜色', '')
                    result = translator.translate(a, dest='ru').text.split('/')
                    # page.write(f"L{row}", result[0])
                    sheet[f"L{row}"] = result[0]
                    column += 1
                    continue
                if '驱动方式' in a:
                    """Привод"""
                    a = a.replace('驱动方式', '')
                    if a == '前置前驱':
                        # page.write(f"K{row}", 'Передний')
                        sheet[f"K{row}"] = 'Передний'
                        continue
                    if a == '后置后驱':
                        # page.write(f"K{row}", 'Задний')
                        sheet[f"K{row}"] = 'Задний'
                        continue
                    if a == '前置四驱':
                        # page.write(f"K{row}", 'Полный')
                        sheet[f"K{row}"] = 'Полный'
                        continue
                    if a == '前置四驱':
                        # page.write(f"K{row}", 'Полный')
                        sheet[f"K{row}"] = 'Полный'
                        continue
                    else:
                        # page.write(f"K{row}", translator.translate(a, dest='ru').text)
                        sheet[f"K{row}"] = translator.translate(a, dest='ru').text
                    column += 1
                    continue
                if '标准容量' in a:
                    """Емкость батареи"""
                    a = a.replace('标准容量', '')
                    # page.write(f"Q{row}", a[:-3])
                    sheet[f"Q{row}"] = a[:-3]
                    column += 1
                    continue
                if '燃油标号' in a:
                    """Марка топлива, тип топлива"""
                    a = a.replace('燃油标号', '')
                    if '92号' or '95号' in a:
                        # page.write(f"O{row}", a.replace('号', ''))
                        sheet[f"O{row}"] = a.replace('号', '')
                        # page.write(f"F{row}", 'Бензин')
                        sheet[f"F{row}"] = 'Бензин'
                    if '0号' in a:
                        # page.write(f"O{row}", a.replace('号', ''))
                        sheet[f"O{row}"] = a.replace('号', '')
                        # page.write(f"F{row}", 'Дизель')
                        sheet[f"F{row}"] = 'Дизель'
                    else:
                        sheet[f"O{row}"] = a.replace('号', '')
                    column += 1
                    continue



    driver_car.close()
    driver_car.quit()


array()
book_update.save('auto_copy.xlsx')
book_update.close()
# book.close()

print("finish")






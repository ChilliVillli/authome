from time import sleep
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from googletrans import Translator
from selenium.webdriver.chrome.options import Options


ua = UserAgent()
headers = {'User-agent': ua.random}
translator = Translator()
chrome_options = Options()
chrome_options.add_argument("--window-size=150,150")


book_update = openpyxl.load_workbook("auto_copy.xlsx")
sheet = book_update.active


row = 1
column = 2
count_two = 0

# d = {2017: count_two, 2018: count_two, 2019: count_two, 2020: count_two,
#      2021: count_two, 2022: count_two, 2023: count_two, 2024: count_two}

names_brend = {'Acura': 'ouge', 'Avatr': 'aweita', 'BAIC': 'beijing', 'Changan': 'changan', 'Chery': 'qirui', 'BAIC_HUS': 'beiqihuansu',
               'Dongfeng': 'dongfeng', 'Exeed': 'xingtu', 'FAW': 'yiqi', 'GAC TRUMPCHI': 'guangqichuanqi',
               'Geely': 'jiliqiche', 'Geely Galaxy': 'jiliyinhe', 'Great Wall': 'changcheng', 'Haval': 'hafu',
               'JAC': 'jiangqijituan', 'Jetour': 'jietu', 'JMC': 'jiangling', 'Kaiyi': 'kaiyi', 'Li': 'lixiangqiche',
               'Livan': 'ruilanqiche', 'Ora': 'oula', 'SWM': 'swmsiweiqiche', 'Tank': 'tanke', 'Venucia': 'qichen',
               'Voyah': 'lantuqiche', 'Wey': 'weipai', 'Zeekr': 'jike', 'Xpeng': 'xiaopeng', 'Dongfengfengshen': 'dongfengfengshen'}

list_url = []

def get_url():
    global row

    ll = sheet[f"C{row+1}"].value

    while ll != None:

        pr = row
        count = 0

        if sheet[f"B{row + 1}"].value != None:
            row += 1
            continue

        if sheet[f"B{row+1}"].value == None:
            name = sheet[f"W{row + 1}"].value
            if name == None:
                row += 1
                continue

            if name == 'all':
                break


            brand = names_brend[sheet[f"A{row + 1}"].value]
            url_cars = f'https://www.che168.com/china/{brand}/{name}/a0_0msdgscncgpi1ltocsp1exx0/'


            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url_cars)
            soup = BeautifulSoup(driver.page_source, 'lxml')

            try:
                auto = soup.find_all('li', class_='cards-li list-photo-li')
                auto += soup.find_all('li', class_='cards-li list-photo-li cxc-card')
            except Exception:

                print(f'Error{brand} {name} {sheet[f"B{row}"].value}')

            driver.close()

            for card in auto:
                count += 1
                book_update.save('auto_copy.xlsx')

                if pr != row:
                    break

                if len(auto) == count:
                    row += 1
                    break

                else:
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

                    if year < 2017:
                        continue

                    if url_work in list_url:
                        continue


                    sheet[f'X{row + 1}'] = carname
                    number_to_remove = ['2017款', '2018款', '2019款', '2020款', '2021款', '2022款', '2023款', '2024款']

                    for symbol in number_to_remove:
                        carname = carname.replace(symbol, "")


                    sheet[f'D{row + 1}'] = year
                    sheet[f'S{row + 1}'] = url_work

                    model = translator.translate(carname, dest='en').text
                    if sheet[f"A{row + 1}"].value not in model:
                        sheet[f'B{row + 1}'] = f'{sheet[f"A{row + 1}"].value} {model}'
                    else:
                        sheet[f'B{row + 1}'] = model
                    sheet[f'V{row + 1}'] = price


                    yield url_work


def array():
    global row, column, page, count

    for url_work in get_url():

        b = ''
        driver_car = webdriver.Chrome(options=chrome_options)
        driver_car.get(url_work)
        card_soup = BeautifulSoup(driver_car.page_source, 'lxml')

        try:
            photo_soup = BeautifulSoup(driver_car.page_source, 'lxml')
            photo_car = photo_soup.find('div', class_='car-pic-list js-box-text').find_all('a')
            provider = card_soup.find('div', class_='merchantCard_right').find_all('span')
            pr = provider[0].text
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
        sheet[f'U{row + 1}'] = b
        auto_card = card_soup.find_all('ul', class_='basic-item-ul')

        list_url.append(url_work)

        row += 1
        column = 2
        print(row)


        for j in auto_card:

            for q in range(len(j.find_all('li'))):

                a = j.find_all('li')[q].text

                try:

                    if '表显里程' in a:
                        """Пробег"""
                        a = a.replace('表显里程', '')
                        result = translator.translate(a, dest='ru').text
                        mileage = ''.join(c if c.isdigit() else '' for c in result).split()
                        mileage = [int(y) for y in mileage]
                        sheet[f'M{row}'] = mileage[0]
                        column += 1
                        continue
                    if '变  速  箱' in a:
                        """Коробка передач"""
                        a = a.replace('变  速  箱', '')
                        result = translator.translate(a, dest='ru').text
                        if result == 'автоматический':
                            sheet[f'J{row}'] = 'АКПП'
                        else:
                            sheet[f'J{row}'] = 'МКПП'
                        column += 1
                        continue
                    if '燃料类型' in a:
                        """Тип двигателя"""
                        sheet[f"F{row}"] = a.replace('燃料类型', '')
                        column += 1
                        continue
                    if 'WLTC纯电续航里程' in a:
                        """Запас хода на электричестве"""
                        a = a.replace('WLTC纯电续航里程', '')
                        sheet[f"R{row}"] = a[:-2]
                        sheet[f"F{row}"] = 'Гибрид'
                        column += 1
                        continue
                    if 'CLTC纯电续航里程' in a:
                        """Запас хода на электричестве"""
                        a = a.replace('CLTC纯电续航里程', '')
                        sheet[f"R{row}"] = a[:-2]
                        sheet[f"F{row}"] = 'Электродвигатель'
                        column += 1
                        continue
                    if 'NEDC纯电续航里程' in a:
                        """Запас хода на электричестве"""
                        a = a.replace('NEDC纯电续航里程', '')
                        sheet[f"R{row}"] = a[:-2]
                        sheet[f"F{row}"] = 'Электродвигатель'
                        column += 1
                        continue
                    if '排       量' in a:
                        """Объем двигателя (л)"""
                        a = a.replace('排       量', '')
                        if 'L' in a:
                            sheet[f"G{row}"] = a.replace('L', '')
                        column += 1
                        continue
                    if '所  在  地' in a:
                        """Город нахождения"""
                        a = a.replace('所  在  地', '')
                        result = translator.translate(a, dest='ru')
                        sheet[f"E{row}"] = result.text
                        column += 1
                        continue
                    if '发  动  机' in a:
                        """Двигатель"""
                        sheet[f"H{row}"] = a.replace('发  动  机', '')
                        a = ''.join(l if l.isdigit() else ' ' for l in a).split()
                        if len(a) == 1:
                            sheet[f"I{row}"] = a[0]
                            column += 1
                            continue
                        if len(a) > 1:
                            sheet[f"I{row}"] = a[2]
                            column += 1
                            continue
                        else:
                            sheet[f"I{row}"] = '-'
                        column += 1
                        continue
                    if '车辆级别' in a:
                        """Класс автомобиля"""
                        a = a.replace('车辆级别', '')
                        result = translator.translate(a, dest='en')
                        sheet[f"N{row}"] = result.text
                        column += 1
                        continue
                    if '车身颜色' in a:
                        """Цвет машины"""
                        a = a.replace('车身颜色', '')
                        result = translator.translate(a, dest='ru').text.split('/')
                        sheet[f"L{row}"] = result[0].title()
                        column += 1
                        continue
                    if '驱动方式' in a:
                        """Привод"""
                        a = a.replace('驱动方式', '')
                        if a == '前置前驱':
                            sheet[f"K{row}"] = 'Передний'
                            continue
                        if a == '后置后驱':
                            sheet[f"K{row}"] = 'Задний'
                            continue
                        if a == '前置四驱':
                            sheet[f"K{row}"] = 'Полный'
                            continue
                        if a == '前置四驱':
                            sheet[f"K{row}"] = 'Полный'
                            continue
                        else:
                            sheet[f"K{row}"] = translator.translate(a, dest='ru').text
                        column += 1
                        continue
                    if '标准容量' in a:
                        """Емкость батареи"""
                        a = a.replace('标准容量', '')
                        sheet[f"Q{row}"] = a[:-3]
                        column += 1
                        continue
                    if '燃油标号' in a:
                        """Марка топлива, тип топлива"""
                        a = a.replace('燃油标号', '')
                        if '92号' or '95号' in a:
                            sheet[f"O{row}"] = a.replace('号', '')
                            sheet[f"F{row}"] = 'Бензин'
                        if '0号' in a:
                            sheet[f"O{row}"] = a.replace('号', '')
                            sheet[f"F{row}"] = 'Дизель'
                        else:
                            sheet[f"O{row}"] = a.replace('号', '')
                        column += 1
                        continue

                except Exception:
                    book_update.save('auto_copy.xlsx')
                    continue

    book_update.save('auto_copy.xlsx')
    driver_car.close()
    driver_car.quit()


array()
book_update.save('auto_copy.xlsx')
book_update.close()

print("finish")






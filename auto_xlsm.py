import xlsxwriter
from autopars import array
from time import sleep


def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\Boris\Desktop\autohome\auto.xlsx")
    page = book.add_worksheet('авто')


    row = 1
    column = 2


    page.write('A1', 'Бренд')
    page.write('B1', 'Название')
    page.write('C1', 'Время листинга')
    page.write('D1', 'Отображение пробега')
    page.write('E1', 'Коробка передач')
    page.write('F1', 'Стандарты выбросов')
    page.write('G1', 'Смещение')
    page.write('H1', 'Ежегодный осмотр')
    page.write('I1', 'Cрок действия страховки истекает')
    page.write('J1', 'Гарантия истекла')
    page.write('K1', 'Обслуживание')
    page.write('L1', 'Двигатель')
    page.write('M1', 'Класс автомобиля')
    page.write('N1', 'Цвет машины')
    page.write('O1', 'Марка топлива')
    page.write('P1', 'Ссылка')
    page.write('Q1', 'Фото')
    page.write('R1', 'Цена')


    # page.write(f'P{row + 1}', url_work)
    # page.write(f'B{row + 1}', carname)
    # page.write(f'R{row + 1}', price)
    # page.write(f'Q{row + 1}', photo)


    for item in parametr():

        page.write(row, column, item)

        column += 1


    book.close()
    print("finish")


writer(array)
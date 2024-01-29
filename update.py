import requests
import openpyxl
from bs4 import BeautifulSoup
from autopars import *
from selenium import webdriver
from time import sleep



book_update = openpyxl.open("auto_copy.xlsx", read_only=True)
sheet = book_update.active


class Row:
    row = 1
    name = ''


def get_url_update():

    Row.row += 1
    name = sheet[f"W{Row.row}"].value

    while sheet[f"S{Row.row}"].value != None:

        url = sheet[f"S{Row.row}"].value
        driver_update = webdriver.Chrome()
        driver_update.get(url)
        sleep(2)
        soup_update = BeautifulSoup(driver_update.page_source, 'lxml')
        tr = soup_update.find('div', class_='wrong_page').find('p').text.strip()
        # er = soup_update.find('div', class_='fail-title').text.strip()

        if tr == '非常抱歉，您访问的车辆信息不存在！':
            get_url()
        else:
            pass


get_url_update()

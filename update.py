import requests
from bs4 import BeautifulSoup
from autopars import *
from selenium import webdriver
from time import sleep


list_url_update = ['https://www.che168.com/dealer/122831/49941535.html', 'https://www.che168.com/dealer/122831/49895809.html',
                   'https://www.che168.com/dealer/541589/49394299.html', 'https://www.che168.com/dealer/559991/49773379.html']



def get_url_update():

    for url in list_url_update:
        driver_update = webdriver.Chrome()
        driver_update.get(url)
        sleep(2)
        soup_update = BeautifulSoup(driver_update.page_source, 'lxml')
        tr = soup_update.find('div', class_='wrong_page').find('p').text.strip()

        if tr == '非常抱歉，您访问的车辆信息不存在！':  #soup_update.find('div', class_='fail-title').text == '加载失败' or
            get_url()

        else:
            pass

get_url_update()

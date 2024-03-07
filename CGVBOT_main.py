from datetime import datetime, date
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import telegram

bot = telegram.Bot(token= 'input your id : input your token')

url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20220824"
#
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
iframes = soup.find_all('iframe')
# for iframe in iframes:
    # response = requests.get(url + iframe['src'])
    # print(response.text)
    # print(iframe)
    #
    # if(iframe['id'] == 'ifrm_movie_time_table'):
    #     print("영화 타임 테이블 발견 ! 주소 : ",iframe['src'])


driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(3)

driver.switch_to.frame("ifrm_movie_time_table")

r = driver.page_source
soup = BeautifulSoup(r,"html.parser")
""" ---------------------------------------------- PARSING DATA END ------------------------------------------------"""

title_list = soup.select('div.info-movie')

imax = soup.select_one('span.imax')

# if(imax):
#
#     Label_date_dataset = imax.find_parent('div',class_='col-times')
#     title_label = Label_date_dataset.select_one('div.info-movie > a > strong').text.strip()
#     print("{} 의 IMAX 예매가 오픈되었습니다.".format(title_label))
#     bot.sendMessage(chat_id=input your id, text="{} 의 IMAX 예매가 오픈되었습니다.".format(title_label))
#
#
#     time_dataset = imax.find_parent('div', class_= 'type-hall')
#     data = time_dataset.findChildren('a')
#
#     for i in data:
#         ymd = i['data-playymd']
#         time = i['data-playstarttime']
#         left_seat =  i['data-seatremaincnt']
#
#         ymd = datetime.strptime(ymd,'%Y%m%d')
#         # time = datetime.strptime(time,'%H%M')
#
#         print("{}월 {}일 /  {} /  잔여좌석 : 624석 / {}석".format(ymd.month,ymd.day, time ,left_seat))
#         bot.sendMessage(chat_id=input your id, text="{}월 {}일 /  {} /  잔여좌석 : {}석 / 624석 ".format(ymd.month,ymd.day, time ,left_seat))
#
#
# else:
#     print("오픈된 IMAX 영화가 없습니다.")



fourdx = soup.select_one('span.forDX')


if(fourdx):
    fourdx = fourdx.find_parent('div', class_= 'col-times')
    title = fourdx.select_one('div.info-movie > a > strong').text.strip()
    bot.sendMessage(chat_id= 'input your id' , text="{} 의 4DX 예매가 오픈되었습니다.".format(title))
else:
    print("오픈된 4DX Screen 2D 영화가 없습니다.")

# for i in title_list:
#     print(i.select_one('a > strong').text.strip())

"""
body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie
body > div > div.sect-showtimes > ul > li:nth-child(2) > div > div.info-movie

"""



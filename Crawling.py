import urllib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import io

from selenium.webdriver.common.keys import Keys

url = "http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013&date=20220729"
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
driver.implicitly_wait(10)

driver.switch_to.frame("ifrm_movie_time_table")

r = driver.page_source
soup = BeautifulSoup(r,"html.parser")
""" ---------------------------------------------- PARSING DATA END ------------------------------------------------"""

title_list = soup.select('div.info-movie')
imax = soup.select_one('span.imax')
fourdx = soup.select_one('span.forDX')

if(imax):
    imax = imax.find_parent('div', class_= 'col-times')
    title = imax.select_one('div.info-movie > a > strong').text.strip()
    print("{} 의 IMAX 예매가 오픈되었습니다.".format(title))
else:
    print("오픈된 IMAX 영화가 없습니다.")

if(fourdx):
    fourdx = fourdx.find_parent('div', class_= 'col-times')
    title = fourdx.select_one('div.info-movie > a > strong').text.strip()
    print("{} 의 4DX Screen 2D 예매가 오픈되었습니다.".format(title))
else:
    print("오픈된 4DX Screen 2D 영화가 없습니다.")

for i in title_list:
    print(i.select_one('a > strong').text.strip())

"""
body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie
body > div > div.sect-showtimes > ul > li:nth-child(2) > div > div.info-movie

"""



"""
날짜 2022.02.28
이름 장현민
내용 파이썬 날씨 데이터 크롤링
"""
import os.path

import  requests as req
from bs4 import  BeautifulSoup as bs
from datetime import  datetime

# 페이지 요청
html = req.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do').text
print(html)
#문서 객체 생성
dom = bs(html, 'html.parser')
print(dom)
# 데이터 파싱
dir = "/home/crawler/weather/{:%Y-%m%d}".format(datetime.now())
if not os.path.exists(dir):
    os.makedirs(dir)
fname = "{:%Y-%m-%d-%H-%M.CSV}".format(datetime.now())
file = open(dir+'/'+fname, 'w', encoding='utf-8')

trs = dom.select('#weather_table > tbody > tr')


for tr in trs:
    t1 = tr.findChildren('td')[0].a.text
    t2 = tr.findChildren('td')[1].text
    t3 = tr.findChildren('td')[2].text
    t4 = tr.findChildren('td')[3].text
    t5 = tr.findChildren('td')[4].text
    t6 = tr.findChildren('td')[5].text
    t7 = tr.findChildren('td')[6].text
    t8 = tr.findChildren('td')[7].text
    t9 = tr.findChildren('td')[8].text
    t10 = tr.findChildren('td')[9].text
    t11 = tr.findChildren('td')[10].text
    t12 = tr.findChildren('td')[11].text
    t13 = tr.findChildren('td')[12].text
    t14 = tr.findChildren('td')[13].text
    print('{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14 ))
# 데이터 파일 저장
file.close()
print('데이터수집완료')


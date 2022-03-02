"""
날짜 2022.02.28
이름 장현민
내용 파이썬 HTML 페이지 요청 실습

    크롤링
    - 웹페이지 데이터를 수집하는 기술
    - 크롤러(봇) 정해진 규칙에 따라 페이지를 이동하면서 데이터를 수집하는 기술

    파식(Parsing)
    - 문서 해독
    - 마크업 문서 (HTML, XML)에서 특정 태그의 데이터를 추출 가공 처리하는 과정
"""

import requests as req
from bs4 import BeautifulSoup as bs

html = req.get('http://chhak.or.kr/test.html').text
print(html)

dom = bs(html, 'html.parser')
print(dom)

title = dom.html.body.h3.text
print('title : ' + title)

rs1 = dom.select_one('#seoul').text
rs2 = dom.select_one('.busan').text
print('rs1 : ' + rs1)
print('rs2 : ' + rs2)


lis = dom.select('ul>li')
for li in lis :
    print('li text :', li.text)

print('=='*100)
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
result = req.get(url, headers={'User-Agent': 'Mozilla//5.0'}).text
print(result)

dom = bs(result, 'html.parser')

tags = dom.select()


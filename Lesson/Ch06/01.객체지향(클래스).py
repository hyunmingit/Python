"""
날짜 2022.01.06
이름 장현민
내용 파이썬 클래스 실습 p148
"""

from Lesson.Lib import Account

kb = Account('국민은행', '101-11-1011', '김유신', 10000)

kb.deposit(30000)
kb.withdraw(10000)


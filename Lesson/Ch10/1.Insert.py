"""
날짜 2022.01.13
이름 장현민
내용 데이터베이스 프로그래밍 p295
"""
import pymysql


#데이터베이스 접속
conn = pymysql.connect(host='54.180.160.240',
               user='jhmcos13',
               password='1234',
               db='jhmcos13',
               charset='utf8')
#SQL실행 객체 생성 (Statement)
cur = conn.cursor()
#SQL실행
sql = "INSERT INTO `User1` VALUES ('P101', '정약용', '010-1212-1010', 43);"
cur.execute(sql)
conn.commit()

#데이터베이스 종료
conn.close()
print('insert complete...')



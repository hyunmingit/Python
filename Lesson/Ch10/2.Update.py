

import pymysql


conn = pymysql.connect(host='54.180.160.240',
               user='jhmcos13',
               password='1234',
               db='jhmcos13',
               charset='utf8')

cur = conn.cursor()



#SQL실행
sql = "UPDATE `User1` SET `age` = `age` +1 WHERE `uid` = 'P101' "
cur.execute(sql)
conn.commit()

#데이터베이스 종료
conn.close()
print('update complete...')




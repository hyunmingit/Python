


import pymysql


conn = pymysql.connect(host='54.180.160.240',
               user='jhmcos13',
               password='1234',
               db='jhmcos13',
               charset='utf8')

cur = conn.cursor()



#SQL실행
sql = "SELECT * FROM `User1`;"
cur.execute(sql)
conn.commit()

#데이터 출력
dataset = cur.fetchall()
#print(dataset) 성의없이나옴

for row in dataset:
    print('=======================')
    print('ID : ', row[0])
    print('Name : ', row[1])
    print('Phone : ', row[2])
    print('Age : ', row[3])
    print('-----------------------')


#데이터베이스 종료
conn.close()
print('select complete...')

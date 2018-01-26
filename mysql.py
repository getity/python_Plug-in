#coding=utf-8
import MySQLdb
import numpy as np

conn = MySQLdb.connect(host='12.23.34.45',port=3306,user='ffff',passwd='123456',db='reclaim')
cur = conn.cursor()
conn.autocommit(1)


query_sql = "select id from reclaim.matchedVideo where created_at < date_sub(now(), interval 1 year);" 
insert_sql = "insert ignore into test.matchedVideoarchived (select * from reclaim.matchedVideo where id = %s);"
delete_sql = "delete from reclaim.matchedVideo where id = %s;"
cur.execute(query_sql)
dataList = cur.fetchall()
aaa = np.array(dataList)
ids = []

for i in range(len(aaa)):
    ids.append(aaa[i])
    if (i+1)%100==0 :
        cur.executemany(insert_sql,ids)
        ids = []

cur.executemany(insert_sql,ids)
ids = []

for i in range(len(aaa)):
    ids.append(aaa[i])
    if (i+1)%100==0 : 
        cur.executemany(delete_sql,ids)
        ids = []

cur.executemany(delete_sql,ids)  
ids = []

cur.close()
conn.close()
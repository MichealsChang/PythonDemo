# coding=utf-8

import datetime

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "iot")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

consId = 200001
key = 1200000
for n in range(1, 2):
    for i in range(1, 10001):
        sql = 'insert into t_bs_b_ms(MS_ID,CONS_ID,MS_NO,TS) values("%d","%d","%s","%s")'
        suffix = "%010d" % i
        msId = str(key) + suffix
        cursor.execute(sql % (long(msId), consId, '1', datetime.datetime.now()))
        db.commit()
    key += 10000

# 关闭数据库连接
db.close()

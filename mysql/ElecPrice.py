# coding=utf-8

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "iot")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for msId in range(11100000000000001, 11100000000000011):
    sql = 'insert into b_a_item_elec_price(KAFKA_MSG_KEY,PSDATE,PEDATE,PRICE,FGP_TYPE,ACTIVE_TIME) ' \
          'values("%d","%s","%s","%f","%s","%s")'
    cursor.execute(sql % (msId, '0000','0300', 1.1, '1', '20171125'))
    cursor.execute(sql % (msId, '0300','0800', 1.2, '2', '20171125'))
    cursor.execute(sql % (msId, '0800','2000', 1.3, '3', '20171125'))
    cursor.execute(sql % (msId, '2000','2300', 1.4, '4', '20171125'))
    cursor.execute(sql % (msId, '2300','2400', 1.5, '5', '20171125'))
    db.commit()

# 关闭数据库连接
db.close()
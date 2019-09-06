# -*- coding:utf-8 -*-
'''
author:zhaoyan
time:2018/11/8 19:54
'''
import pymysql

#建立数据库连接
conn = pymysql.connect(host='rdscd16cciucbiyeqb2dw.mysql.rds.aliyuncs.com',
                    port=3306,
                    user='zaozuo',
                    passwd='test2014',
                    db='zaozuo_canal',
                    charset='utf8')
#从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

#查询数据库（读）
cur.execute("SELECT * FROM item WHERE item_id=(SELECT item_id FROM `sku` WHERE sku_id='22491'")
result = cur.fetchall()
print(result)
# L = []
# for i in range(result):
#     L.append()
#     i += 1
# print(L)
#更改数据库（写）
#cur.execute("delect from")

#提交更改
conn.commit()

#关闭游标及连接
cur.close()
conn.close()

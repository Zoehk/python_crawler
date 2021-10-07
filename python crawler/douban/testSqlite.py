# -*- coding =utf-8 -*-
# @Time : 2021/10/6 13:56
# @Author : woquan
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3
# 1.连接数据库
conn = sqlite3.connect("test.db") # 打开或创建数据库文件
print("Opened database successfully!")

# # 2.创建数据表
# c = conn.cursor() # 获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
# c.execute(sql) # 执行sql语句
# conn.commit() # 提交数据库操作
# conn.close() # 关闭数据库操作
# print("成功建表")


# # 3.插入数据
# c = conn.cursor() # 获取游标
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values(2,'张三',32,"成都",8000)
# '''
# sql3 = '''
#     insert into company (id,name,age,address,salary)
#     values(3,'李四',23,"九江",3000)
# '''
# c.execute(sql2) # 执行sql语句
# c.execute(sql3) # 执行sql语句
# conn.commit() # 提交数据库操作
# conn.close() # 关闭数据库操作
# print("插入数据完毕")

# 4.查询数据
c = conn.cursor() # 获取游标
sql = "select id,name,address,salary from company"
cursor = c.execute(sql) # 执行sql语句
for row in cursor:
    print("id= ", row[0])
    print("name= ", row[1])
    print("address= ", row[2])
    print("salary= ", row[3], "\n")
conn.commit() # 提交数据库操作
conn.close() # 关闭数据库操作
print("插入数据完毕")

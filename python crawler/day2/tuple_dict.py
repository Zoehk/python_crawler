#-*- coding =utf-8 -*-
#@Time : 2021/9/20 10:54
#@Author : woquan
#@File : tuple_dict.py
#@Software : PyCharm

######### 列表和字典是重点

# Tuple(元组):其元素不可以修改
# tup1 = ()
# tup2 = (50,60,70)
# print(type(tup2))# <class 'tuple'>
# print(tup2[-1]) # 倒着访问元组,访问最后一个元素
# print(tup2[1:3]) # 左闭右开

# 增
# tup3 = (22,34,532)
# tup4 = ("132","5434")
# tup = tup3+tup4
# print(tup)

# 删
# tup5 = ("132", "5434", 23, 243)
# del tup5 # 删除了整个元组元素
# print(tup5)

# 改：无法修改其中的元素




#####
# dict:基本无法修改
# info = {"name":"吴彦祖","age":18}
# print(info["name"])
# print(info["age"])
# # print(info["gender"]) # 访问了不存在的键，直接访问报错
# print(info.get("gender")) # 使用get方法，无法找到对应的键，会默认返回：none
# print(info.get("gender","m")) # 没找到的话，可以设定默认值


# 增：
# info = {"name":"吴彦祖","age":18}
# newID = input("请输入新的学号")
# info["id"] = newID
# print(info["id"])


# 删:
# 【del】
# info = {"name":"吴彦祖","age":18}
# print("删除前：%s"%info["name"])
# del info["name"]
# print("删除后：%s"%info["name"])
# info = {"name":"吴彦祖","age":18}
# print("删除前：%s"%info)
# del info
# print("删除后：%s"%info) # 删除字典后会报错，del 语句可以运行
# 【clear】
# info = {"name":"吴彦祖","age":18}
# print("清空前：%s"%info)
# info.clear()
# print("清空后：%s"%info) # 删除字典后会报错，del 语句可以运行


# 改:
# info = {"name":"吴彦祖","age":18}
# info["age"]=20
# print(info) # 删除字典后会报错，del 语句可以运行


# 查：（遍历）
# info = {"ID":1,"name":"吴彦祖","age":18}
# print(info.keys()) # 得到所有的键（列表）
# print(info.values()) # 得到所有的值（列表）
# print(info.items()) # 得到所有的项（列表），每个键值对是一个元组

# 遍历所有的键
info = {"ID":1,"name":"吴彦祖","age":18}
for key in info.keys():
    print(key)
# 遍历所有的值
for value in info.values():
    print(value)
# 遍历所有的项
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))

# 使用枚举函数，同时拿到列表中的下标和元素内容
list = ["a","b","c","d","e"]
for i,x in enumerate(list):
    print(i,x)

# set:集合（不可以重复）

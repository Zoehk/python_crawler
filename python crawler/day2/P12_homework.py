#-*- coding =utf-8 -*-
#@Time : 2021/9/20 16:33
#@Author : woquan
#@File : P12_homework.py
#@Software : PyCharm

# # Q1: # 打印一条横线
# def line():
#     print("-"*20)
# line()
#
# # Q2: # 打印a条横线
# def times(a):
#     while a>0:
#         line()
#         a-=1
# times(3)
#
# # Q3：求三个数的和
# def sum(a,b,c):
#     sum=a+b+c
#     return sum
# sum(1,2,3)
#
# # Q4:
# def average(a,b,c):
#     average=sum(a,b,c)/3
#     return average
# print(average(1,2,3))
#
# # 全局变量和局部变量
#
# def test1():
#     a=300 # 局部变量
#     print("test1---修改前：a=%d"%a)
#     a=100
#     print("test1---修改后：a=%d"%a)

# 在函数中修改全局变量
a=100
def test3():
    global a  # 声明全局变量在函数中的标识符
    print("test1---修改前：a=%d"%a)
    a=300
    print("test1---修改后：a=%d"%a)
test3()
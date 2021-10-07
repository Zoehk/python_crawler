# -*- coding =utf-8 -*-
# @Time : 2021/9/25 22:50
# @Author : woquan
# @File : demo1.py
# @Software : PyCharm

# f = open("test.txt","w") # 打开文件，w模式，文件不存在就新建文件
# f.write("hello world, I am here!") # 将字符串写入文件中
# # f = open("test.txt","r") # 打开文件，r模式，以只读方式打开文件
# # f = open("test.txt","a") # 打开一个文件用于追加，文件已存在，文件指针放于文件的结尾。不存在则新建
# f.close() # 关闭文件

# f = open("test.txt","r")
# content = f.read(5)
# print(content)
# content = f.read(6) # 每执行一次，向后移动一定数目。
# print(content)
# content = f.readlines() # 读完整个文档
# print(content)
# i=1
# for temp in content:
#     print("%d:%s"%(i,temp)) # 输出文本中每一行字符内容
#     i += 1
# f.close() # 读取5个字符

# f = open("test.txt","r")
# content = f.readline()
# print("1:%s"%content,end="") # 文件读取时同样是按行操作，end=""可以不换行
# content = f.readline()
# print("2:%s"%content)
# f.close()

# import os # python中的os模块中重命名、删除等一些操作
# os.rename("test.txt","test1.txt") # 文件重命名

# 捕获异常
# try：
#     print("----test1----")
#     f = open("123.txt","r") # 用只读模式打开了一个不存在的文件，报错
#     print("----test2----") # 该句代码不会被执行


# try:
#     print("----test1----")
#     f = open("123.txt","r") # 用只读模式打开了一个不存在的文件，报错
#     print("----test2----") # 该句代码不会被执行
# except IOError: # 输入和输出的错误就忽略，文件没找到属于IO异常
#     pass

# try:
#     print(num)
# # except IOError:
# except NameError: # 异常类型想要被捕获，需要一致
#     print("产生错误了")

'''
try:
    print("----test1----")
    f = open("123.txt","r") # 用只读模式打开了一个不存在的文件，报错
    print("----test2----") # 该句代码不会被执行
    print(num)
except (NameError,IOError): # 将所有可能产的异常类型都放在小括号当中
    print("产生错误了")
'''
import time

'''
# 获取错误描述
try:
    print("----test1----")
    f = open("test1.txt", "r") # 用只读模式打开了一个不存在的文件，报错
    print("----test2----") # 该句代码不会被执行
    print(num)
except (NameError,IOError) as result: # 将所有可能产的异常类型都放在小括号当中
    print("产生错误了")
    print(result)
'''

'''
# 捕获所有的异常
try:
    print("----test1----")
    f = open("1.txt", "r") # 用只读模式打开了一个不存在的文件，报错
    print("----test2----") # 该句代码不会被执行
    print(num)
except Exception as result: # exception可以承接任何异常
    print("产生错误了")
    print(result)
'''

# try....finally 和嵌套
import time
try:
    f = open("test1.txt","r")
    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("发生异常。。。")

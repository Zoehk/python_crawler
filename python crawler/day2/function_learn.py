#-*- coding =utf-8 -*-
#@Time : 2021/9/20 16:22
#@Author : woquan
#@File : function_learn.py
#@Software : PyCharm

'''
# 函数的定义
def printinfo():
    print("--------------------------------")
    print(" 人生苦短，我用python  ")
    print("--------------------------------")

# 函数的调用
printinfo()
'''

'''
# 带参数的函数
def add2Num(a,b):
    c=a+b
    print(c)

add2Num(11,34)
'''

'''
# 带返回值的函数
def add2Num(a,b):
    return  a+b  # 通过return来返回运算结果
c=add2Num(11,22)
print(c)

# 返回多个值的函数
def divid(a,b):
    shang = a//b
    yushu = a%b
    return shang,yushu
sh,yu = divid(11,2)
print("商：%d,余数：%d"%(sh,yu))
'''


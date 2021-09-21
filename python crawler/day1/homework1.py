#-*- coding =utf-8 -*-
#@Time : 2021/9/17 15:51
#@Author : woquan
#@File : homework1.py
#@Software : PyCharm

enter=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
import random
x=random.randint(0,2)
print("随机生成数字为：%d" %x)
if enter>=0 and enter<=2:
    if enter==x:
        print("平局")
    elif enter-x==-2 or enter-x==1:
        print("哈哈，我赢了")
    elif enter==-1 or enter-x==2:
        print("害，我输了！")
else:
    print("输入无效")


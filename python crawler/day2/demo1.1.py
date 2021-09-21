#-*- coding =utf-8 -*-
#@Time : 2021/9/20 8:38
#@Author : woquan
#@File : demo1.1.py
#@Software : PyCharm

import random #输入random
offices=[[],[],[]] #设置空列表
names=["a","b","c","d","e","f","g"] #老师名字
#分配
for name in names:
    i=random.randint(0,len(offices)-1)
    offices[i].append(name)

j=1
for office in offices:
    print("办公室%d的人数为：%d"%(j,len(office)))
    j+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)

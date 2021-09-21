#-*- coding =utf-8 -*-
#@Time : 2021/9/18 21:13
#@Author : woquan
#@File : homework2.py
#@Software : PyCharm

# 打印九九乘法表
for i in range(1,10):# 最大到9
    print("\t")
    for j in range(1,i+1):# 最大到i
        print("%d*%d=%d"%(i, j, i*j), end=" ")
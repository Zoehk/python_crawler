#-*- coding =utf-8 -*-
#@Time : 2021/9/17 16:40
#@Author : woquan
#@File : demo4.py
#@Software : PyCharm

'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,10,3):
    print(i)
'''

'''
name="chengdu"
for x in name:
    #print(x)
    print(x,end="\t")
    print(x,end=" ")
'''

'''
a=["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''

'''
# 写循环体结构
i=0
while i<5:
    print("当前是第%d次循环"%(i+1))
    i+=1
'''

'''
# 1-100求和
i=1;
sum=0;
while i<101: 
    sum+=i
    i+=1
print(sum)
'''

'''
count=0
while count<5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")
'''

'''
# 用break打印1——10：break会直接跳出for和while循环
n=1
while n<100: 
    if n>10:
        break
    print(n)
    n+=1
'''


'''
# continue会直接跳出当前循环，直接进入下一轮
# 例1：
n=0
while n<10:
    n = n + 1
    if n%2==0:
        continue
    print(n)
'''

'''
# pass的运用:用作占位语句，不做任何事情
for letter in "Room":
    if letter=="o":
        pass
        print("pass")
    print(letter)

'''


'''

'''






#-*- coding =utf-8 -*-
#@Time : 2021/9/19 8:36
#@Author : woquan
#@File : list.py
#@Software : PyCharm

'''
namelist =[]# 定义一个空的列表
namelist=["小张","小王","小李"]
testlist=[1,"测试"] # 列表中可以存储混合类型
print(namelist[1])
print(type(testlist[1]))
print(type(testlist[0]))
'''

'''
namelist=["小张","小王","小李"]
for name in namelist:
    print(name)
print(len(namelist))

length =len(namelist)
i=0
while i<length:
    print(namelist[i])
    i+=1

# 增：【appen】
print("---增加前，名单列表的数据")
for name in namelist:
    print(name)

nametemp=input("输入追加的名单：")
namelist.append(nametemp)
print("---增加后，名单列表的数据")
for name in namelist:
    print(name)
'''

'''
a=[1,2]
b=[3,4]
a.append(b) #将列表当成一个元素，添加到a列表中
print(a)
a.extend(b) # 将b的每个元素，逐一追加
print(a)
'''

'''
# 增：【insert】指定下标位置插入元素
a=[1,2,3]
a.insert(0,0) # 第一个变量表示下标，第二个变量表示元素（对象）
print(a) 
'''

'''
# 删【del】
moviename=["1","2","3","1"]
print("---删除前，名单列表的数据")
for name in moviename:
    print(name)

# del moviename[2] # 删除指定位置的元素
# moviename.pop() # 弹出末尾最后一个元素
moviename.remove("1") # 直接删除指定的内容,对于内容重复的列表，只删除第一个
print("---删除后，名单列表的数据")
for name in moviename:
    print(name)
'''

'''
# 改：
moviename=["1","2","3","1"]
print("---改前，名单列表的数据")
for name in moviename:
    print(name)
moviename[1]="xiaohong" 
print("---改后，名单列表的数据")
for name in moviename:
    print(name)
'''

'''
# 查：
namelist=["小张","小王","小李"]
findName =input("要查找的学生名字")
if findName in namelist:
    print("找到了")
else:
    print("未找到")
'''

'''
mylist=["a","b","c","a","b"]
print(mylist.index("a",1,4)) # 可以查找指定下标范围内的元素，并返回找到对应数据的下标 
print(mylist.index("a",1,5)) # 范围是左闭右开
print(mylist.count("a")) # 查找相应元素的个数
'''

'''
##### 排序和反转
a=[1,5,6,2,3]
a.reverse() # 将列表所有元素翻转
print(a)
a.sort()
print(a) # 升序排序
a.sort(reverse=True)
print(a) # 降序排列
'''

# schoolName =[[],[],[]] # 有三个元素的空列表，每个元素都是一个空列表
schoolName=[["北京大学","清华大学"],["南开大学","天津大学","天津理工大学"]]
print(schoolName[0])
print(schoolName[0][0])
for i in range(len(schoolName[0])):
    print(i,schoolName[0][i])

##### 把老师分配到三个办公室(明天新建文件重新来一下)
import random
offices=[[],[],[]]
names=["A","B","C","D","E","F","G"]
for name in names:
    index =random.randint(0,2)
    offices[index].append(name)

i=1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)


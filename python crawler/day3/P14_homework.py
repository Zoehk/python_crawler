# -*- coding =utf-8 -*-
# @Time : 2021/9/27 19:42
# @Author : woquan
# @File : P14_homework.py
# @Software : PyCharm

################################### 做法一 #####################################
# 写古诗
'''
f = open("gushi.txt","w",encoding="utf-8") # 中文采用utf-8编码
f.write("""
        静夜思
         李白
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。""")
f.close() # 之前就忘记关闭文件了
# 复制古诗到txt文档
f = open("gushi.txt", "r", encoding="utf-8") # 读取文件r
g = open("copy.txt", "w", encoding="utf-8") # 写入文件w
content = f.readlines() # 把所有的文件都读取出来
for i in content:
    g.write(i)
print("复制完毕")
f.close()
g.close()
'''
################################### 做法二 #####################################
def writeFile(filename, content):
    f = open("filename", "w",encoding="utf-8")
    for i in content:
        f.write(i)
    f.close()

def readFile(filename):
    f = open("filename", "r", encoding="utf-8")
    contents = f.readlines()
    return contents
    f.close()

gushi = [日照香炉生紫烟\n, 遥看瀑布挂前川\n, 飞流直下三千尺\n, 疑似银河落九天\n]
writeFile(gushi.txt, gushi)
contents = readFile(gushi.txt)
copy = []
for content in contents:
    copy.append(content)
writeFile(copy.txt, copy)
# -*- coding =utf-8 -*-
# @Time : 2021/9/28 8:36
# @Author : woquan
# @File : spider.py
# @Software : PyCharm

'''
def main(a):
    print("hello",a)
main(2)
if __name__=="__main__":  # 用来测试代码，防止其他模块的代码引入时自动执行
    # 调用函数
    main(1)
'''

# from day3 import demo1 # 引入自定义模块
# print(demo1.add(3,5))

# 引入系统模块
import sys
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行Excel操作
import sqlite3  # 进行SQLite3数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    #savepath = "豆瓣电影top250.xls"
    # # 3.1保存数据在excel中
    # saveData(datalist, savepath)
    # 3.2 保存数据在数据库中
    dbpath = "movie.db"
    saveData2(datalist, dbpath)


# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">') # 生成正则表达式对象，表示规则（字符串的模式）
# 影片图片
findImaSrc = re.compile(r'<img .*src="(.*?)"', re.S) # re.S 让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
fingJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)



# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range (0, 10): # 调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"): # 查找符合要求的字符串，形成列表
            data = []
            item = str(item)
            # 获取影片超链接
            link = re.findall(findLink, item)[0] # re库通过正则表达式来查找指定的字符串
            data.append(link) # 添加链接
            imgSrc = re.findall(findImaSrc, item)[0]
            data.append(imgSrc) # 添加图片
            titles = re.findall(findTitle, item)
            if(len(titles)==2):
                ctitle = titles[0] # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "") # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ') # 外国名留空
            rating = re.findall(findRating, item)[0]
            data.append(rating) # 添加评分
            judgeNum = re.findall(fingJudge, item)[0]
            data.append(judgeNum) # 添加评价人数
            inq = re.findall(findInq, item) # 概述有可能没有，分类讨论
            if (len(inq))!=0:
                inq = inq[0].replace("。","") # 去掉句号
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)/>(\s+)?'," ",bd) # 去掉<br/>
            bd = re.sub('/'," ",bd)
            data.append(bd.strip()) # 去掉前后的空格
            datalist.append(data) # 把处理好的一部电影信息放入datalist
    print(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
    # 用户代理，告诉豆瓣服务器，本质上是告诉浏览器告诉浏览器，我们可以接收什么水平的文件
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html



# 保存数据在Excel中
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建workbook对象
    sheet = book.add_sheet('doubantop250',cell_overwrite_ok=True) # 创建工作表
    col = ("电影链接", "图片链接", "电影中文名", "电影外国名", "评分", "评价数目", "概况", "相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) # 列名
    for i in range(0,250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j]) # 数据
    book.save(savepath)

# 保存数据在数据库中
def saveData2(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    ''' # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":  # 用来测试代码，防止其他模块的代码引入时自动执行
    # 调用函数
    main()
    print("爬取完毕")



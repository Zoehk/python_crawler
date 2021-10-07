# -*- coding =utf-8 -*-
# @Time : 2021/9/30 9:17
# @Author : woquan
# @File : testUrllib.py
# @Software : PyCharm

# 1.点开网页，点击F12就可以查看网页源码;2.点击network，点击网络流，找到对应的网站，点击headers

import urllib.request
# 获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8')) # 对获取到的网页进行utf-8的解码


# # 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding="utf-8")#  把所有的数据转换为二进制的数值
# response1 = urllib.request.urlopen("http://httpbin.org/post", data = data) # post用来封装数据
# print(response1.read().decode("utf-8"))

# 超时处理
# try:
#     response2 = urllib.request.urlopen("http://httpbin.org/post",timeout=0.01)
#     print(response2.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status) # 状态码
# response = urllib.request.urlopen("http://douban.com")
# print(response.status) # 报错，发现了是爬虫
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheader("Server")) # 获取具体的反应头部


# 访问举例
# url = "http://httpbin.org/post"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
# # 在这里进行了伪装，模拟真实浏览器的行为
# data = bytes(urllib.parse.urlencode({'name':'eric'}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


# 访问豆瓣
# url = "http://www.douban.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
# # 在这里进行了伪装，模拟真实浏览器的行为
# req = urllib.request.Request(url=url, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))



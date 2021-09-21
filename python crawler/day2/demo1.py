#-*- coding =utf-8 -*-
#@Time : 2021/9/19 8:12
#@Author : woquan
#@File : demo1.py
#@Software : PyCharm

'''
word='字符串'
sentence="这是一个句子"
my_str="he said\"i love you \""
my_str1='he said "i love you"'
paragraph="""
          这是一个段落
          可以多行展示
          """
print(word)
print(sentence)
print(my_str)
print(my_str1)
print(paragraph)
'''
##### \\反斜杠符号； \'单引号； \"双引号； \n换行

##### 只截取字符串的一部分
str= "chengdu"
print(str)
print(str[0:6])
print(str[1:7:2]) # [起始位置：结束位置：步进值]
print(str[:5])
print(str +",你好！") # 多个字符串连接
print(str*3)
print("hello\nNanchang") # \n是换行
print(r"hello\nNanchang") # 在字符串前面加一个r,表示直接显示原始字符串，不进行转义


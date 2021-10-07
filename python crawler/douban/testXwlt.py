# -*- coding =utf-8 -*-
# @Time : 2021/10/5 16:49
# @Author : woquan
# @File : testXwlt.py
# @Software : PyCharm

# homework:把九九乘法表对应到excel文件中
import xlwt
workbook = xlwt.Workbook(encoding="utf-8") # 创建workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建工作表
for i in range(1, 10):
    print('\t')
    for j in range(1, i+1):
        worksheet.write(i-1, j-1, "%d*%d=%d"%(i, j, i*j)) # 写入数据
workbook.save('student.xls')
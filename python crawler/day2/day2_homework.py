#-*- coding =utf-8 -*-
#@Time : 2021/9/20 9:01
#@Author : woquan
#@File : day2_homework.py
#@Software : PyCharm

# 输出一个商品列表
products =[["iphone",6888],["MacPro",14888],["小米6",2499],["Coffee",3],["Book",60]]
print("-"*5,"商品列表","-"*5)
i=0
j=0
for list in products:
    i += 1
    print(i, end="\t")
    for j in range(len(list)):
        print(list[j],end="\t") # end="\t"表示不换行
    print("\t")

cart=[]
price=0
while 1:
    user=input("请输入要购买的商品编号(按q键结束购物)：")
    if user!="q" and (0-1)<int(user)<(len(products)+1):
        user = int(user)
        cart.append(products[user-1][0])
        price += products[user-1][1]
        print("请问还需要其他的商品吗？（若无，按q键结束购物）：")
    elif user == "q":
        print("您购买的商品有：",end="\n")
        for i in cart:
            print(i, end="、")
        print("\b")
        print("一共%d元，谢谢光临！" %price)
        break
    else:
        print("您输入的商品编号不存在，请重新输入：")


from flask import Flask, render_template,request
import datetime
app = Flask(__name__)

# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!你好,欢迎光临'
# debug模式开启：点击左上方的flaskdemo——》edit configuration——》flask_debug

@app.route('/index')
def hello():  # put application's code here
    return 'Hello World!你好,欢迎光临'

# 通过访问路径，获取用户的字符串参数
@app.route("/user/<name>")
def welcom(name):
    return "你好，%s"%name

# 通过访问路径，获取用户的整形参数，此外还有float类型
@app.route("/user/<int:id>")
def welcome(id):
    # return "hello，%d"%id+"号的会员"
    return "hello，%d号的会员"%id

# 返回给用户渲染后的网页文件
@app.route("/")
def index2():
    return render_template("index.html")

# 向页面传递一些变量
@app.route("/1")
def index3():
    time = datetime.date.today() # 普通变量
    name = ["Li","Zhang","Wang"] # 列表类型
    task = {"任务:":"打扫卫生","时间:":"3小时"} # 字典变量
    return render_template("index.html", var = time, list = name, task =task)

# 表单提交
@app.route("/test/register")
def register():
    return render_template("test/register.html")

# 接收表单提交到路由，需要指定的methods为post
@app.route("/result", methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)

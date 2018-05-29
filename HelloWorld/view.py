from django.http import HttpResponse
from django.shortcuts import render
from HelloWorld import connectdb


def hello(request):
    # return HttpResponse("hello world!")
    context = {}
    context['hello'] = 'Hello World!'
    nums = [1, 2, 3]
    context['nums'] = nums
    db = connectdb.connectMysql()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("select * from user")
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    context['datas'] = data
    print(data)
    # 关闭数据库连接
    db.close()
    return render(request, 'hello.html', context)


def login(request):
    return render(request, 'login.html', None)

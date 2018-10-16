from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
import json
from django.core import  serializers


def login_views(request):
    if request.method == 'GET':
        if 'id' in request.session and 'uphone' in request.session:
            return HttpResponseRedirect('/index/')
        else:
            if 'id' in request.COOKIES and 'uphone' in request.COOKIES:
                request.session['id'] = request.COOKIES['id']
                request.session['uphone'] = request.COOKIES['uphone']
                return HttpResponseRedirect('/index/')
            form = LoginForm()
            return render(request, 'fruitday_login.html', locals())
    else:
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']
        uList = User.objects.filter(uphone=uphone,upwd=upwd)
        if uList: # 登录成功,保存session
            request.session['uphone'] = uphone
            request.session['id'] = uList[0].id
            resp = HttpResponseRedirect('/index/')
            if 'isSaved' in request.POST:
                # 记住密码
                resp.set_cookie('id',uList[0].id,60*60*24*365)
                resp.set_cookie('uphone',uphone,60*60*24*365)
            return resp
        else:
            form = LoginForm()
            return render(request, 'fruitday_login.html',
             locals())


def register_views(request):
    if request.method == 'GET':
        return render(request, 'fruitday_regist.html')
    else:
        uphone = request.POST['uphone']
        uList = User.objects.filter(uphone=uphone)
        if uList:
            return
        upwd = request.POST['upwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        dict = {'uphone':uphone, 
        'upwd':upwd,
        'uname':uname,
        'uemail':uemail}
        user = User(**dict)
        user.save()
    return HttpResponse('注册成功')

def index_views(request):
    return render(request, 'index.html', locals())


def goods_views(request):
    goodstypes = GoodsType.objects.all()
    lst = []
    for type in goodstypes:
        dic={}
        dic['type'] = json.dumps(type.to_dict())
        goods = type.goods_set.order_by("-id")[0:5]
        goodsAjax = serializers.serialize('json', goods)
        dic['goods']=goodsAjax
        lst.append(dic)
    Ajax = json.dumps(lst)

    return HttpResponse(Ajax)

def logout_views(request):
    del request.session['id']
    del request.session['uphone']
    return HttpResponseRedirect('/login/')

def check_uphone_views(request):
    uphone = request.GET["uphone"]
    uList = User.objects.filter(uphone=uphone)
    if uList:
        s = 1
        msg = "用户名称已存在"
    else:
        s = 0
        msg = "通过"
    dic = {"status":s, "msg":msg}
    return HttpResponse(json.dumps(dic))
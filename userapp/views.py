import hashlib

import datetime
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from userapp.captcha.image import ImageCaptcha
from homeapp.models import User, Check_user
import random,string,re

# Create your views here.
from xiangmu import settings


def login(request):
    flag = request.GET.get("flag")
    return render(request,'login.html',{'flag':flag})

def loginlogic(request):
    flag = request.GET.get('flag')
    txtusername = request.POST.get('txtusername')
    txtpassword = request.POST.get('txtpassword')
    user = User.objects.filter(email=txtusername)
    if user:
        nickname = user[0].nickname
        txtyan = User.objects.filter(email=txtusername)[0].extend
        sault = txtpassword + txtyan
        h = hashlib.md5()
        h.update(sault.encode())
        two_pwd = h.hexdigest()
        result = User.objects.filter(email=txtusername,password=two_pwd)
        if result and flag=="1":
            request.session['login'] = user[0].id
            return redirect('categoryapp:indent')
        elif result and flag=='None':
            url = reverse('homeapp:index')+'?nickname='+nickname+'&stus=1'
            request.session['login'] = user[0].id
            return redirect(url)
    else:
        return redirect('userapp:login')

def register(request):
    flag = request.GET.get("flag")
    return render(request,'register.html',{'flag':flag})

def regist_1(request):
    flag = request.GET.get("flag")
    username = request.POST.get('username')
    names = request.POST.get('names')
    userpwd = request.POST.get('userpwd')
    code = request.session.get('code')
    if User.objects.get(username=username):
        return redirect('userapp:register')
    else:
        user_1 = User.objects.create(email=username,nickname=names,password=userpwd)
        if code.lower() == request.POST.get('identifycode').lower() and flag == "1":
            return redirect("categoryapp:indent")
        elif code.lower() == request.POST.get('identifycode').lower() and flag != "1":
            return redirect('homeapp:index')

def getcaptcha(request):
    imaage = ImageCaptcha()
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    random_code = ''.join(code)
    request.session['code'] = random_code
    data = imaage.generate(random_code)
    return HttpResponse(data,'image/png')

def hu(request):
    username = request.GET.get("username")
    res = User.objects.filter(email=username)
    if res:
        return HttpResponse('no')
    elif not username:
        return HttpResponse('em')
    else:
        if not re.findall('\w+@[0-9a-zA-Z]{2,3}\.com|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',username):
            return HttpResponse('terr')
        else:
            return HttpResponse('yes')

def mi(request):
    userpwd2 = request.GET.get("userpwd2")
    userpwd1 = request.GET.get("userpwd1")
    if userpwd2 != userpwd1:
        return HttpResponse('n')
    elif not userpwd2:
        return HttpResponse('n')
    elif not userpwd1:
        return HttpResponse('n')
    else:
        return HttpResponse('o')

def yan(request):
    identifycode = request.GET.get("identifycode")
    ni = request.session.get('code')
    if not identifycode:
        return HttpResponse('em')
    elif identifycode.lower() != ni.lower():
        return HttpResponse('no')
    else:
        return HttpResponse('yes')

def registerok(request):
    username = request.session.get('username')
    nickname1 = User.objects.get(email=username).nickname
    return render(request,'register ok.html',{'username':username,'nickname1':nickname1})

def salt():
    l = 'qwertyuiop[]lkjkdjdhhfdgfhsdnsbccbvvxxznmxmx.,'
    salt = ''.join(random.sample(l,6))
    return salt


def has_code(email,now):
    h = hashlib.md5()
    email += now
    h.update(email.encode())
    return h.hexdigest()

def make_check_user(new_user):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = has_code(new_user.email,now)
    Check_user.objects.create(code=code,user=new_user)
    return code


def send_email(email,code):
    subject='来自DD的邮件'
    from_email = 'ypf9112115@sina.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target=blank>www.baidu.com</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1',code)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def registerok_1(request):
    username = request.POST.get('username')
    pwd = request.POST.get('userpwd')
    pwd2 = request.POST.get('userpwd2')
    nic = request.POST.get('nickname1')
    code = request.POST.get('txt_vcode')
    x = salt()
    sault = pwd + x
    h = hashlib.md5()
    h.update(sault.encode())
    two_pwd = h.hexdigest()
    u = User.objects.filter(email=username)
    res = re.findall('\w+@[0-9a-zA-Z]{2,3}\.com|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',username)
    if u:
        redirect('userapp:register')
    else:
        if res and pwd == pwd2 and code.lower() == request.session.get('code').lower():
            new_user = User.objects.create(email=username,extend=x,password=two_pwd,nickname=nic)
            new_user.save()
            code = make_check_user(new_user)
            send_email(username, code)
            request.session['username'] = username
            return redirect('userapp:registerok')
        else:
            return redirect('userapp:register')



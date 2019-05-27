from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from carapp.car import Buycar, Item
from homeapp.models import Product
from homeapp.models import User
# Create your views here.

def carlist(request):
    cart = request.session.get('cart')
    res = render(request,'car.html',{'cart':cart})
    return res

def addcar(request):
    bid = request.GET.get('bid')
    bobj = Product.objects.filter(id=bid)[0]
    cart = request.session.get('cart')
    if not cart:
        cart = Buycar()
    item = Item(bobj,1)
    cart.add(item)
    request.session['cart'] = cart
    return HttpResponse('ok')

def upcar(request):
    iid = request.GET.get('item_id')
    new_count = int(request.GET.get('new_count'))
    cart = request.session.get('cart')
    cart.upc(iid,new_count)
    request.session['cart'] = cart
    s1 = cart.upc(iid,new_count)
    s2 = cart.allprice
    s3 = cart.count
    s4 = cart.save
    js = {'s1':s1,'s2':s2,'s3':s3,'s4':s4}
    return JsonResponse(js)

def car_remove(request):
    info_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    cart.remove(info_id)
    request.session['cart'] = cart
    s2 = cart.allprice
    s3 = cart.count
    s4 = cart.save
    js = {'s2': s2, 's3': s3, 's4': s4}
    return JsonResponse(js)

def car_logic(request):
    userid = request.session.get('login')
    if userid:
        return redirect('categoryapp:indent')
    else:
        url = reverse("userapp:login")+"?flag=1"
        return redirect(url)


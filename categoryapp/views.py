from django.shortcuts import render
from homeapp.models import Product, Address
import re

# Create your views here.
def booklist(request):
    return render(request,'booklist.html')

def booklist_1(request):
    b_id = request.GET.get('b_id')
    p = Product.objects.get(id=b_id)
    return render(request,'Book details.html',{'p':p,'b_id':b_id})

def indent_ok(request):
    return render(request,'indent ok.html')

def indentlogic(request):
    ship_man = request.GET.get('ship_man')
    ship_site = request.GET.get('ship_site')
    ship_mail = request.GET.get('ship_mail')
    ship_phone = request.GET.get('ship_phone')
    ship_cellphone = request.GET.get('ship_cellphone')
    ship_variable = Address.objects.filter(consignee=ship_man,detailaddress=ship_site,postalcode=ship_mail,telephone=ship_phone,mobilephone=ship_cellphone)
    if not ship_variable:
        cart = request.session.get('cart')
        # if not re.findall('\w+|^138\d{8}$|^159\d{8}$|^136\d{8}$|^171\d{8}$|^177\d{8}$|^149\d{8}$|^183\d{8}$',ship_phone) and re.findall('\w|^010\d{8}$|^0132\d{7}$',ship_cellphone):
        Address.objects.create(consignee=ship_man,detailaddress=ship_site,postalcode=ship_mail,telephone=ship_phone,mobilephone=ship_cellphone)
        return render(request,'indent ok.html',{'ship_variable':ship_variable,'cart':cart})
    else:
        cart = request.session.get('cart')
        return render(request,'indent.html',{'ship_variable':ship_variable,'cart':cart})

def indent(request):
    cart = request.session.get('cart')
    return render(request,'indent.html',{'cart':cart})
from django.shortcuts import render
from homeapp.models import Category,Product
from django.core.paginator import Paginator

# Create your views here.
def booklist1(request):
    bookl_1 = Category.objects.filter(id__in=range(1,14))
    bookl_2 = Category.objects.filter(id__in=range(14,62))
    bookl_3 = request.GET.get('one_id')
    bookl_4 = request.GET.get('two_id')
    num1 = request.GET.get('num1')
    num = request.GET.get('page')
    if not num:
        num = 1
    elif num1:
        num = num1
    if bookl_3 and bookl_4 == 'None'or bookl_3 and bookl_4 is None:
        g1 = Category.objects.get(id=bookl_3)
        b = Product.objects.filter(cate__parent_id__in=bookl_3)
        pagtor = Paginator(b,per_page=3)
        page = pagtor.page(num)
        return render(request, 'booklist.html',
                      {'bookl_1': bookl_1, 'bookl_2': bookl_2, 'page': page, 'bookl_3': bookl_3, 'bookl_4': bookl_4,'stu':1,'g1':g1,'pagtor':pagtor
                       })
    elif bookl_4 and  bookl_3 == 'None'or bookl_4 and  bookl_3 is None:
        g2 = Category.objects.get(id=bookl_4)
        og1 = Category.objects.get(id=g2.parent_id)
        bb = Product.objects.filter(cate=bookl_4)
        pagtor = Paginator(bb, per_page=3)
        page = pagtor.page(num)
        return render(request,'booklist.html',{'bookl_1': bookl_1, 'bookl_2' : bookl_2, 'page' :page, 'bookl_3': bookl_3, 'bookl_4': bookl_4,'stu':2,'og1':og1,'g2':g2,'pagtor':pagtor})



from django.shortcuts import render
from homeapp.models import Category,Product

# Create your views here.
def index(request):
    cate1 = Category.objects.filter(id__in=range(1,14))
    cate2 = Category.objects.filter(id__in=range(14,62))
    cate3 = Product .objects.all()[:8]
    cate4 = Product.objects.all()[9:18]
    cate5 = Product.objects.all()[19:30]
    cate6 = Product.objects.all()[:5]
    cate7 = Product.objects.all()[:10]
    nickname = request.GET.get('nickname')
    stus=request.GET.get('stus')
    print(stus)
    return render(request,'index.html',{'nickname':nickname,'cate1':cate1,'cate2':cate2,'cate3':cate3,'cate4':cate4,'cate5':cate5,'cate6':cate6,'cate7':cate7,'stus':stus})

def index_1(request):
    return





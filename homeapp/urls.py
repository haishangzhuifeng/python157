from django.urls import path
from homeapp import views

app_name = 'homeapp'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('index_1/',views.index_1,name='index_1'),
]
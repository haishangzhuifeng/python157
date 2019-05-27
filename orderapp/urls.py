from django.urls import path
from orderapp import views

app_name = 'orderapp'
urlpatterns = [
    path('booklist1/',views.booklist1,name='booklist1'),
]
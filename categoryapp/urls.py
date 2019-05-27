from django.urls import path
from categoryapp import views

app_name = 'categoryapp'
urlpatterns = [
    path('booklist/',views.booklist,name='booklist'),
    path('booklist_1/',views.booklist_1,name='booklist_1'),
    path('indent_ok/',views.indent_ok,name='indent_ok'),
    path('indentlogic/',views.indentlogic,name='indentlogic'),
    path('indent/', views.indent, name='indent'),
]
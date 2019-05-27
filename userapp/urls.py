from django.urls import path
from userapp import views

app_name = 'userapp'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('register/',views.register,name='register'),
    path('regist_1/',views.regist_1,name='regist_1'),
    path('getcaptcha/', views.getcaptcha, name='getcaptcha'),
    path('hu/', views.hu, name='hu'),
    path('mi/', views.mi, name='mi'),
    path('yan/', views.yan, name='yan'),
    path('registerok/', views.registerok, name='registerok'),
    path('registerok_1/', views.registerok_1, name='registerok_1'),
]
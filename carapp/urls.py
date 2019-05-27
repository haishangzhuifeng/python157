from django.urls import path
from carapp import views

app_name = 'carapp'
urlpatterns = [
    path('carlist/',views.carlist,name='carlist'),
    path('addcar/',views.addcar,name='addcar'),
    path('upcar/',views.upcar,name='upcar'),
    path('car_remove/',views.car_remove,name='car_remove'),
    path('car_logic/',views.car_logic,name='car_logic'),
   ]
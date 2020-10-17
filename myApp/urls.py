from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('div.html', views.div),
    path('refresh11/', views.refresh11),
    path('refresh13/', views.refresh13),
    path('refresh21/', views.refresh21),
    path('refresh23/', views.refresh23),
    path('refresh31/', views.refresh31),
    path('refresh33/', views.refresh33),
    path('map/', views.map)
]
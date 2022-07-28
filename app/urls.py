from django.urls import path
from . import views

urlpatterns = [
    path('', views.deshboard, name='Deshboard'),
    path('home/', views.home, name='Home'),
    path('bgimage/', views.bgimage, name='BGImage'),
    path('bgvideo/', views.bgvideo, name='BGVideo'),
   path('section/', views.section, name='Section'),
] 
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('hello_pet/<str:pet>/', views.hello_pet),
    path('hello_calculate/<int:y>/', views.hello_calculate),
    path('show_them/<str:pet>/', views.show_them),
    path('show_them/<str:pet>/skills', views.show_them),
    path('show_them/<str:pet>/food', views.food),
    path('show_them/<str:pet>/contact', views.contact),
    path('show_them/<str:pet>/about', views.about),
]

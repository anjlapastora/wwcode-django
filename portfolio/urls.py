from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
	# Basic Urls
    path('hello/', views.hello),
    path('<str:pet>/', views.hello_pet),
    path('pets_age/<int:y>/', views.pets_age),

    # URLs with templates
    path('show/<str:pet>/', views.show_pet),
    path('show/<str:loc>/home/', views.show_home),
    path('show/<str:pet>/skills/', views.show_skills),
    path('show/<str:pet>/food/', views.food),

    path('page/contact/', views.contact),
    path('page/home/', views.home),
    path('page/about/', views.about),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
	path('home/', views.home),
	path('signup/', views.register),
	path('login/', views.login),
]
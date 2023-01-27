from django.contrib import admin
from django.urls import path,include
from myApp import views

urlpatterns = [
    path("", views.create_short_url, name="create_short_url"),
    path("login", views.loginuser, name="login"),
    path("logout", views.logoutuser, name="logout"),
    path("signup",views.signupuser,name="signup"),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.delete_url, name='delete_url'),
    path('<str:shortenedd>', views.redirect_url, name='redirect_url'),
]

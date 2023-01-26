from django.contrib import admin
from django.urls import path,include
from myApp import views

urlpatterns = [
    path("", views.create_short_url, name="create_short_url"),
    path('<str:shortenedd>', views.redirect_url, name='redirect_url'),
]

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='mmk-shop-login'),
    path('userAuth/', views.userAuth, name='mmk-shop-userAuth'),

    path('', views.index, name='mmk-shop-index'),
]

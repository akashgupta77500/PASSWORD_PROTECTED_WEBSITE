from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.login, name="login"),
    path('api', views.api, name="api"),
    path('logout', views.logout_logout, name="logout_logout"),

]

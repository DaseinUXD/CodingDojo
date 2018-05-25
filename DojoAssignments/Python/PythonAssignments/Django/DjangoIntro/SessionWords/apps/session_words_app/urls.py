from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^index/', views.index),
    url(r'^add/', views.add),
    url(r'^clear/', views.clear),
]


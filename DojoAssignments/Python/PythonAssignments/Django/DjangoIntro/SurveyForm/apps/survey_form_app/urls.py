from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^result/$', views.result),
    url(r'^submission/$', views.submission),
    url(r'^goBack/$', views.goBack),
]


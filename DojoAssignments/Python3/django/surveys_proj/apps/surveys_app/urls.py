from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^submission/$', views.submission),
    url(r'^result/$', views.result),
    url(r'^goBack/$', views.goBack),


]
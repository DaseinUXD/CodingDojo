from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^log_in/$', views.login),
    url(r'^books/$', views.books),
    url(r'^add/$', views.add),
    url(r'^reviews/$', views.reviews),
    url(r'^user/$', views.user),

]
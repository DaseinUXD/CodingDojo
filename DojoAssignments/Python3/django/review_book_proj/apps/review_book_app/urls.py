from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^books/$', views.books),
    url(r'^books/add/$', views.add),
    url(r'^books/(?P<id>\d+)/$', views.book),
    url(r'^add_book/$', views.add_book),
    url(r'^reviews/$', views.reviews),
    url(r'^add_review/(?P<id>\d+)/$', views.add_review),
    url(r'^users/(?P<id>\d+)/$', views.user),
    url(r'^logout/$', views.logout),

]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# Index view

def index(request):
    return render(request, 'session_words_app/index.html')

def add(request):
    if request.method=="POST":

        return redirect('/')
    else:
        # do something else
        return redirect('/')

def clear(request):
    return redirect('/')
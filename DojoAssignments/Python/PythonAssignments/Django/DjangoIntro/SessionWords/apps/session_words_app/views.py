# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# Index view

def index(request):
    return render(request, 'session_words_app/index.html')

def add(request):
    return redirect('/')

def clear(request):
    return redirect('/')
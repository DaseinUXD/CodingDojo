# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from .classes import attemptCounter

# Create your views here.



def index(request):
    count = attemptCounter(1)
    request.count = count.increment()


    context = {
        "attemptNumber": request.count,

        "randomWord": get_random_string(14)
    }
    return render(request, 'random_word/index.html', context)

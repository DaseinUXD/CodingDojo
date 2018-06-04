# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, "survey_form_app/index.html")





def submission(request):
    request.session['count'] = request.POST['count']
    request.session['name'] = request.POST['name']
    request.session['city'] = request.POST['city']
    request.session['lang'] = request.POST['lang']
    request.session['comments'] = request.POST['comments']
    return redirect(result)


def result(request):
    print("I went through the submission function to the result page")
    return render(request, "survey_form_app/result.html")


def goBack(request):
    # request.session['count'] = request.POST['count']
    return render("survey_form_app/index.html")

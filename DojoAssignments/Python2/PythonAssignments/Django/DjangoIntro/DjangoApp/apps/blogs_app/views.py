# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    response = "Placeholder to later display a list of all blogs"
    return HttpResponse(response)


def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)


def create(request):
    return redirect('/')


def show(request, number):
    response = "Placeholder to display blog number: " + number
    return HttpResponse(response)


def edit(request, number):
    response = "Placeholder to edit blog number: " + number
    return HttpResponse(response)


def delete(request, number):
    response = "Placeholder to delete blog number: " + number
    return HttpResponse(response)
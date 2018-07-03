from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    context = {"Placeholder text": "place"}

    return render(request, 'review_book_app/index.html', context)


# Create your views here.
def register(request):
    response = "Placeholder text"

    return HttpResponse(response)


# Create your views here.
def login(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Create your views here.
def books(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Create your views here.
def add(request):
    context = {}
    return render(request, 'review_book_app/add.html', context)


# Create your views here.
def reviews(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Create your views here.
def user(request):
    response = "Placeholder text"
    return HttpResponse(response)

from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book

# Create your views here.
def index(request):

    user = Book.objects.first().uploaded_by

    print(user)

    book = User.objects.first()

    print(book)



    return HttpResponse(user, book)



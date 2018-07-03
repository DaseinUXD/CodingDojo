from django.shortcuts import render, HttpResponse, redirect

from django.urls import reverse
from django.contrib import messages

from .models import User, Book, Review

import datetime
import bcrypt



# Create your views here.
# Default view
def index(request):
    return render(request, 'review_book_app/index.html')

# Register user
def register(request):
    print('im in the register function')
    print(request.method)
    if request.method == 'POST':
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']

        print(name)
        errors = User.objects.register(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        else:
            User.objects.create(name=name, alias=alias, email=email, password=password)

    return redirect('/')

# Process login request
def login(request):
    email_login = request.POST['email_login']
    print(email_login)
    request.session['email_login'] = email_login

    return redirect('/books')


# Display books.
def books(request):
    email_login = request.session['email_login']
    user = User.objects.get(email = email_login)
    print(user.id)
    print(user.name)
    all_books = Book.objects.all()
    print(all_books)
    all_reviews = Review.objects.all()
    print(all_reviews)
    # print(review, review.book.title, review.book.author, review.reviewer.alias, review.content, review.rating)

    context = {
        'name': user.name,
        'alias': user.alias,
        'email': user.email,
        'books': all_books,
        'reviews': all_reviews,



    }

    return render(request,'review_book_app/books.html', context)

def book(request, id):
    all_books = Book.objects.all()
    # print(all_books)
    # print(all_books.get(id=2))
    all_reviews = Review.objects.all()
    set_reviews = Review.objects.filter(book_id=id)
    print(set_reviews)
    # print(all_reviews)
    all_users = User.objects.all()
    # print(all_users)
    book = Book.objects.get(id=id)
    # print(book, book.title)
    context = {
        'books': all_books,
        'all_reviews': all_reviews,
        'set_reviews': set_reviews,
        'users': all_users,
        'book': book,
        'id': id,
    }

    return render(request,'review_book_app/book.html', context)


# Display add a book form.
def add(request):
    all_books = Book.objects.all()


    context = {
        'books':all_books,
    }
    return render(request, 'review_book_app/add.html', context)


# Process adding book and review.
def add_book(request):
    context = {}
    return redirect ('/books')


# View reviews by a user.
def reviews(request):
    response = "Placeholder text"
    return HttpResponse(response)

def add_review(request, id):

    return redirect('/books')


# Create your views here.
def user(request, id):
    user = User.objects.get(id=id)
    reviews = Review.objects.filter(reviewer=user)
    print(reviews)
    count = len(reviews)
    print(count)
    context = {
        'user': user,
        'reviews': reviews,
        'count': count,
    }

    return render (request, 'review_book_app/user.html', context)

# Process logout request
def logout(request):

    return redirect('/')
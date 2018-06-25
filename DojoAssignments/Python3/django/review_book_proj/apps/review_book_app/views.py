from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# Default view
def index(request):
    context= {'Placeholder text':'place'}
    return render(request, 'review_book_app/index.html', context)
# Register user
def register(request):
    return redirect('/')

# Process login request
def login(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Display books.
def books(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Display add a book form.
def add(request):
    context = {}
    return render(request, 'review_book_app/add.html', context)


# Process adding book and review.
def add_book(request):
    context = {}
    return redirect ('/books')


# View reviews by a user.
def reviews(request):
    response = "Placeholder text"
    return HttpResponse(response)


# Create your views here.
def user(request):
    response = "Placeholder text"
    return HttpResponse(response)

# Process logout request
def logout(request):

    return redirect('/')
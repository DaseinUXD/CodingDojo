from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# Default view
def index(request):
    return render(request, 'review_book_app/index.html')

# Register user
def register(request):
    print('made it to register')
    return redirect('/')

# Process login request
def login(request):

    return redirect('/books')


# Display books.
def books(request):

    return render(request,'review_book_app/books.html')

def book(request):

    return render(request,'review_book_app/book.html')


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

def add_review(request):
    return redirect('/books')


# Create your views here.
def user(request):
    response = "Placeholder text"
    return HttpResponse(response)

# Process logout request
def logout(request):

    return redirect('/')
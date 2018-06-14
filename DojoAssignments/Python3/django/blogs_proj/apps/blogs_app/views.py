from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Placeholder to later display all the list of blogs"
    return render(request, 'blogs_app/index.html')

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method=='POST':
        print("*"*80)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"
        print("*"*80)
        return redirect('/')
    else:
        return redirect('/')


def show(request, number):
    response = "Placeholder to display {}".format(number)
    return HttpResponse(response, number)

def edit(request, number):
    response = "Placeholder to edit blog {}".format(number)
    return HttpResponse(response, number)

def destroy(request, number):
    response = "Delete"
    return redirect('/')
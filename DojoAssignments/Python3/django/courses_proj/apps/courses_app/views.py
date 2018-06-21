from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    response = "Placeholder text"
    return render(request, 'courses_app/index.html')


def destroy(request):
    i = 4
    return redirect('/')
    # return render(request, 'courses_app/destroy.html')

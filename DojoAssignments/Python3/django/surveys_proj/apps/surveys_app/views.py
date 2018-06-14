from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request,'surveys_app/index.html')

def submission(request):
    if request.method == 'POST':
        print("+"*80)
        print(request.POST)
        print("+"*80)
        return redirect('/result/')
    else:
        return redirect('/')

def result(request):
    print(request.POST)
    return render(request, 'surveys_app/result.html')

def goBack(request):

    return redirect('/')
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request,'surveys_app/index.html')

def submission(request):
    if request.method == 'POST':
        print("+"*80)
        print(request.POST)
        print(request.POST['city'])
        print("+"*80)
        request.session['name']=request.POST['name']
        request.session['city']=request.POST['city']
        request.session['lang']=request.POST['lang']
        request.session['comments']=request.POST['comments']
        # establishes the counter for submissions
        count = request.session.get('count', 0)
        request.session['count'] = count + 1

        return redirect('/result/')
    else:
        return redirect('/result')

def result(request):
    print("*"*80)
    print(request.session)
    print(request.session['count'])
    print(request.session['name'])
    print(request.session['city'])
    print(request.session['lang'])
    print(request.session['comments'])
    print("*"*80)


    # Allows the simplification of only {{var}}
    #  on html page vs {{request.session.var}}
    # context is a dictionary with key:value pairs passed to the render method
    context = {
        'count': request.session['count'],
        'name': request.session['name'],
        'city': request.session['city'],
        'lang': request.session['lang'],
        'comments': request.session['comments'],

    }



    return render(request, 'surveys_app/result.html', context)

def goBack(request):

    return redirect('/')


from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string


# Create your views here.

def index(request):
    return render(request, 'random_word_app/index.html')


def random_word(request):
    if request.method == "POST":
        print("*" * 80)
        print(request.POST)
        # print(request.POST['name'])
        # request.session['name'] = 'test'
        print("*" * 80)
        word = get_random_string(14, 'abcdefghijklmnopqrstuvwxyz0123456789')
        request.session['word'] = word
        print(word)
        attempt = request.session.get('attempt', 0)
        request.session['attempt'] = attempt + 1
        return redirect('/')
    else:
        return redirect('/')


def reset(request):
    del request.session['attempt']
    del request.session['word']
    return redirect('/')

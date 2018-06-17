from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, time, strftime, localtime
from datetime import date, datetime
import json
from decimal import Decimal
now = datetime.now()
# Create your views here.
# Index / root
def index(request):
    print(request.method)
    if request.method=='GET':
        session_on = (request.session.get('session_on'))
        new_word = (request.session.get('new_word'))
        color_choice = (request.session.get('color_choice'))
        font_size = (request.session.get('font_size'))
        time = (request.session.get('time'))
        date = (request.session.get('date'))
    else:
        return False
    context = {
        'session_on':session_on,
        'new_word':new_word,
        'color_choice':color_choice,
        'font_size':font_size,
        'time':time,
        'date':date,
    }
    print(session_on, new_word, color_choice, font_size, time, date)



    return render(request, 'session_words_app/index.html', context)

#  add a word with certain settings
def add_word(request):
    if request.method == 'POST':
        request.session['session_on'] = True

        print("+" * 80)
        print(request.POST)
        print(request.session)
        print("+" * 80)


        if request.POST.get('font_size') == None:
            request.session['font_size'] = 6
        # elif request.POST.get('font_size') == 1:
        #     request.session['font_size'] = 1
        else:
            request.session['font_size'] = 1

        request.session['new_word'] = request.POST['new_word']
        request.session['color_choice'] = request.POST['color_choice']
        # dy = str(now.weekday())
        # dt = int(strftime('%d'))
        # m = str(now.month)
        # y = str(now.year)
        d = strftime('%d').lstrip('0').replace(' 0', ' ')
        first = strftime('%A, %B %dst %Y').lstrip('0').replace(' 0', ' ')
        second = strftime('%A, %B %dnd %Y').lstrip('0').replace(' 0', ' ')
        third = strftime('%A, %B %drd %Y').lstrip('0').replace(' 0', ' ')
        n_th = strftime('%A, %B %dth %Y').lstrip('0').replace(' 0', ' ')
        # di = int(now.day)
        # ds = str(now.day)
        # print(dy, dt, m, y, d)
        if d == '1' or d == '21' or d == '31':
            date = first
        elif d == '2' or d == '22':
            date = second
        elif d == '3' or d == '23':
            date = third
        else:
            date = n_th
        request.session['date'] =date
        request.session['time'] = strftime('%I:%M:%S %p %Z', localtime()).lstrip('0').replace(' 0', ' ')

        page_data = {
            'new_word': request.session['new_word'],
            'color_choice': request.session['color_choice'],
            'font_size': request.session['font_size'],
            "time": time,
            "date": date,
        }





        return redirect('/')
    else:
        request.session['session_on'] = False
        return redirect('/')


def clear(request):
    response = "clear"
    return HttpResponse(response)

from django.shortcuts import render
from time import gmtime, time, strftime
from datetime import date
# Create your views here.

def index(request):
    gmt = gmtime()
    print(gmt)
    print(type(gmt))

    date_time = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": date.today(),
    }
    return render(request,'time_display_app/index.html', date_time)

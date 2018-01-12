from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello_world(request):
    a = 'heeeej'
    return HttpResponse(a)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Teraz: %s.</body></html>" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Za %s godz, będzie: %s.</body></html>" %(offset, dt)

    return HttpResponse(html)
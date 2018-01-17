from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from django.urls import reverse

class MojeView(View):
    def post(self, request, info):
        a = 'heeeej'
        return HttpResponse(a)

    def get(self, request):
        a = 'heeeej'
        reverse('moje')
        return HttpResponse(a)


def hello_world(request):
    a = 'heeeej'
    return HttpResponse(a)

def index(request):
    context = { 'user': 'Jan Kowalski'}
    return render(request, 'base.html', context)



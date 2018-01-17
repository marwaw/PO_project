from django.shortcuts import render
from django.views import View


class Base(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'base.html', context)


class Topics(View):
    def get(self, request):
        return render(request, 'tematy/listy_tematow.html')




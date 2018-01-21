from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import OptionsForm
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO

class Topics(View):
    def post(self, request):
        form = OptionsForm(request.POST)
        if not form.is_valid():
            return redirect("topics_options")

        filters = {'nauczycielakademickiid__nazwisko__contains': form.cleaned_data['name']}
        if form.cleaned_data['topic_options'] == 'free':
            filters['czywolny'] = 1
        tematy = []
        for temat in Temat.objects.all().filter(**filters):
            status = 'wolny' if temat.czywolny else 'zajęty'
            tematy.append(TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid), status))

        context = {'user': 'Jan Kowalski', 'tematy': tematy}
        return render(request, 'tematy/listy_tematow.html', context)

class Topics_Options(View):
    def get(self, request):
        form = OptionsForm()
        context = {'user': 'Jan Kowalski', 'form' : form}

        return render(request, 'tematy/opcje_przegladania.html', context)
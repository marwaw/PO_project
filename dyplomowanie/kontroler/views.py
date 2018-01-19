from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from dyplomowanie.model.Deklaracja import DeclarationForm
from .forms import NameForm, DeclarationForm2



class Base(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'base.html', context)


class Topics(View):
    def get(self, request):
        tematy = [('temat1', 'promotor1', 'wolny'), ('temat2', 'promotor1', 'wolny'), ('temat3', 'promotor2', 'zajety')]
        context = {'user': 'Jan Kowalski', 'tematy': tematy}
        return render(request, 'tematy/listy_tematow.html', context)

class Topics_Options(View):
    def get(self, request):

        if request.method == 'POST':
            form = NameForm(request.POST)
        else:
            form = NameForm()

        context = {'user': 'Jan Kowalski', 'form' : form}

        return render(request, 'tematy/opcje_przegladania.html', context)


class Work(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'moja_praca.html', context)

class Declaration(View):
    def get(self, request):

        student_info = \
            {'name': 'Jan',
             'surname': 'Kowalski',
             'subject': 'Informatyka',
             'speciality' : '-',
             'studies_more': 'I stopień, studia dzienne, III rok',
             'topic_PL': 'Temat temat',
             'topic_ENG': 'Topic topic',
             'supervisor': 'Adamczyk Adam'}

        form = DeclarationForm()
        context = {'user': 'Jan Kowalski', 'form': form}
        return render(request, 'deklaracja/deklaracja.html', context)

    def post(self, request):
        student_info = \
            {'name': 'Jan',
             'surname': 'Kowalski',
             'subject': 'Informatyka',
             'speciality': '-',
             'studies_more': 'I stopień, studia dzienne, III rok',
             'topic_PL': 'Temat temat',
             'topic_ENG': 'Topic topic',
             'supervisor': 'Adamczyk Adam'}

        form = DeclarationForm(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['opis'])






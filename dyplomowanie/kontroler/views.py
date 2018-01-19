from django.shortcuts import render
from django.views import View

from .forms import NameForm, DeclarationForm


class Base(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
        return render(request, 'base.html', context)


class Topics(View):
    def get(self, request):
        context = {'user': 'Jan Kowalski'}
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

        if request.method == 'POST':
            form = DeclarationForm(request.POST)
        else:
            form = DeclarationForm(student_info)

        context = {'user': 'Jan Kowalski', 'form': form}
        return render(request, 'deklaracja/deklaracja.html', context)




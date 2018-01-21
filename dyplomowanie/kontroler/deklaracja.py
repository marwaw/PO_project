from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import DeclarationForm2

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

        form = DeclarationForm2(student_info)
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

        form = DeclarationForm2(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['opis'])
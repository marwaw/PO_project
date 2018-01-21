from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from dyplomowanie.model.Student import Student
from .forms import DeclarationForm2

class Declaration(View):
    def get(self, request):
        student = Student.objects.get(id = 2)

        student_info = {
            'name': student.imie,
            'surname': student.nazwisko,
            'subject': student.kierunekstudiow,
            'speciality' : student.specjalnosc,
            'studies_more': f'{student.stopienstudiow} stopień, studia {student.formastudiow}, {student.rokstudiow} rok',
            'topic_PL': student.tematid.trescpl,
            'topic_ENG': student.tematid.tresceng,
            'supervisor': f'{student.tematid.nauczycielakademickiid.imie} {student.tematid.nauczycielakademickiid.nazwisko}' }

        form = DeclarationForm2(student_info)
        context = {'user': f'{student.imie} {student.nazwisko}', 'form': form}
        return render(request, 'deklaracja/deklaracja.html', context)

    def post(self, request):
        student = Student.objects.get(id=2)

        student_info = {
            'name': student.imie,
            'surname': student.nazwisko,
            'subject': student.kierunekstudiow,
            'speciality': student.specjalnosc,
            'studies_more': f'{student.stopienstudiow} stopień, studia {student.formastudiow}, {student.rokstudiow} rok',
            'topic_PL': student.tematid.trescpl,
            'topic_ENG': student.tematid.tresceng,
            'supervisor': f'{student.tematid.nauczycielakademickiid.imie} {student.tematid.nauczycielakademickiid.nazwisko}'}
        form = DeclarationForm2(request.POST)
        if form.is_valid():
            return HttpResponse(form.cleaned_data['description'])
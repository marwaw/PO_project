from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.Student import Student
from .forms import OptionsForm, TopicForm
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO

class Topics(View):
    def post(self, request):
        student = Student.objects.get(id=1)
        success = False
        temat_wybrany = True

        form = TopicForm(request.POST)
        if not form.is_valid():
            temat_wybrany = False
            form = OptionsForm(request.POST)
            if not form.is_valid():
                return redirect("topics_options")

        if temat_wybrany:
            student.tematid = Temat.objects.get(id=form.cleaned_data['topic_id'])
            student.save()
            success = True

        filters = {'nauczycielakademickiid__nazwisko__contains': form.cleaned_data['name']}
        if form.cleaned_data['topic_options'] == 'free':
            filters['czywolny'] = 1
        tematy = []
        for temat in Temat.objects.all().filter(**filters):
            status = 'wolny' if temat.czywolny else 'zajęty'
            tematy.append(TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid), status))

        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid)
        context = {'user': student, 'tematy': tematy, 'success': success}
        return render(request, 'tematy/listy_tematow.html', context)

class Topics_Options(View):
    def get(self, request):
        student = Student.objects.get(id=1)

        form = OptionsForm()
        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid)
        context = {'user': student, 'form' : form}

        return render(request, 'tematy/opcje_przegladania.html', context)
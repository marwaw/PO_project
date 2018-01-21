from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.model.Deklaracja import DeclarationForm
from dyplomowanie.model.Student import Student
from .forms import OptionsForm, DeclarationForm2
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO


class Base(View):
    def get(self, request):
        student = Student.objects.get(id=2)

        context = {f'{student.imie} {student.nazwisko}'}
        return render(request, 'base.html', context)


class Work(View):
    def get(self, request):
        student = Student.objects.get(id=2)
        temat = None
        if student.tematid:
            temat = Temat.objects.get(id = student.tematid.id)
            temat = TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid))

        context = {'user': f'{student.imie} {student.nazwisko}', 'temat': temat}
        return render(request, 'moja_praca.html', context)








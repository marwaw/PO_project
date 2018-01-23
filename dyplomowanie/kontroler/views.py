from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.Deklaracja import DeclarationForm
from dyplomowanie.model.Student import Student
from .forms import OptionsForm, DeclarationForm2
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO


class Base(View):
    """
    Kontroler bazowy.
    Template: widok/base.html
    """
    def get(self, request):
        student = Student.objects.get(id=1)
        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid)

        context = {'user': student}
        return render(request, 'base.html', context)


class Work(View):
    """
    Kontroler zakładki "Moja praca"
    Template: widok/moja_praca.html
    """
    def get(self, request):
        """
        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'temat': temat -
                1) jeśli student ma wybrany temat - obiekt DTO opisujący ten temat
                2) w przeciwnym przypadku None
        :param request:
        :return:
        """
        student = Student.objects.get(id=1)

        temat = None
        if student.tematid:
            temat = Temat.objects.get(id = student.tematid.id)
            temat = TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid))

        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid, student.deklaracja_set.count())
        context = {'user': student, 'temat': temat}
        return render(request, 'moja_praca.html', context)








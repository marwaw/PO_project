from django.shortcuts import render
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.Student import Student
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO

STUD_ID = 1


class Base(View):
    """
    Kontroler bazowy.
    Template: widok/base.html
    """
    student = Student.objects.get(id=STUD_ID)

    def get(self, request):
        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid)

        context = {'user': student_dto}
        return render(request, 'base.html', context)


class Work(View):
    """
    Kontroler zakładki "Moja praca"
    Template: widok/moja_praca.html
    """

    student = Student.objects.get(id=STUD_ID)

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

        temat = None
        if self.student.tematid:
            temat = Temat.objects.get(id=self.student.tematid.id)
            temat = TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid))

        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid, self.student.deklaracja_set.count())
        context = {'user': student_dto, 'temat': temat}
        return render(request, 'moja_praca.html', context)

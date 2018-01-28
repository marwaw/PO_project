from django.shortcuts import render
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.Deklaracja import Deklaracja
from dyplomowanie.model.Student import Student
from .forms import DeclarationForm

STUD_ID = 1


class Declaration(View):
    """
    Kontroler odpowiadający za widok formularza deklaracji
    Widok: widok/deklaracja/deklaracja.html
    """

    student = Student.objects.get(id=STUD_ID)

    def get(self, request):
        """
        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'form': form - formularz, który ma zostać wyświetlony
            (wypełniony podstawowymi danymi o studencie i wybranym przez niego temacie)
        :param request: żadanie http GET
        :return: Powoduje wyrenderowanie się widoku deklaracja.html, wraz z danymi z context
        """

        student_info = {
            'name': self.student.imie,
            'surname': self.student.nazwisko,
            'subject': self.student.kierunekstudiow,
            'speciality': self.student.specjalnosc,
            'studies_more': f'{self.student.stopienstudiow} stopień, studia {self.student.formastudiow}, {self.student.rokstudiow} rok',
            'topic_PL': self.student.tematid.trescpl,
            'topic_ENG': self.student.tematid.tresceng,
            'supervisor': f'{self.student.tematid.nauczycielakademickiid.imie} {self.student.tematid.nauczycielakademickiid.nazwisko}'}

        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid, self.student.deklaracja_set.count())
        form = DeclarationForm(student_info)
        context = {'user': student_dto, 'form': form}
        return render(request, 'deklaracja/deklaracja.html', context)

    def post(self, request):
        """
        Po otrzymaniu formularza następuje zapisanie informacji o złożonej przez
        studenta deklaracji.
        context:
            'user': student - obiekt DTO, przechowujące najważniejsze dane o studencie
            'form': form - formularz, który ma zostać wyświetlony
            (wypełniony danymi, które zostały przesłane metodą POST)
        :param request: żądanie HTTP POST
        :return: Powoduje wyrenderowanie się widoku deklaracja.html, wraz z danymi z context
        """

        form = DeclarationForm(request.POST)
        success = False

        if form.is_valid():
            deklaracja = Deklaracja(tematid=self.student.tematid, studentid=self.student,
                                    celizakres=form.cleaned_data['goal'],
                                    opis=form.cleaned_data['description'])
            deklaracja.save()
            success = True

        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid, self.student.deklaracja_set.count())
        context = {'user': student_dto, 'form': form, 'success': success}
        return render(request, 'deklaracja/deklaracja.html', context)

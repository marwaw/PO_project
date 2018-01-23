from django.shortcuts import render
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.Deklaracja import Deklaracja
from dyplomowanie.model.Student import Student
from .forms import DeclarationForm2

class Declaration(View):
    """
    Kontroler odpowiadający za widok formularza deklaracji
    Widok: widok/deklaracja/deklaracja.html
    """
    def get(self, request):
        """
        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'form': form - formularz, który ma zostać wyświetlony
            (wypełniony podstawowymi danymi o studencie i wybranym przez niego temacie)
        :param request: żadanie http GET (???)
        :return: Powoduje wyrenderowanie się widoku deklaracja.html, wraz z danymi z context
        """
        student = Student.objects.get(id=1)

        student_info = {
            'name': student.imie,
            'surname': student.nazwisko,
            'subject': student.kierunekstudiow,
            'speciality' : student.specjalnosc,
            'studies_more': f'{student.stopienstudiow} stopień, studia {student.formastudiow}, {student.rokstudiow} rok',
            'topic_PL': student.tematid.trescpl,
            'topic_ENG': student.tematid.tresceng,
            'supervisor': f'{student.tematid.nauczycielakademickiid.imie} {student.tematid.nauczycielakademickiid.nazwisko}' }

        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid, student.deklaracja_set.count())
        form = DeclarationForm2(student_info)
        context = {'user': student, 'form': form}
        return render(request, 'deklaracja/deklaracja.html', context)

    def post(self, request):
        """
        Po otrzymaniu formularza następuje zapisanie informacji o złożonej przez
        studenta deklaracji.
        context:
            'user': student - obiekt DTO, przechowujące najważniejsze dane o studencie
            'form': form - formularz, który ma zostać wyświetlony
            (wypełniony danymi, które zostały przesłane metodą POST)
        :param request: żadanie HTTP POST
        :return: Powoduje wyrenderowanie się widoku deklaracja.html, wraz z danymi z context
        """
        student = Student.objects.get(id=1)
        form = DeclarationForm2(request.POST)
        success = False

        if form.is_valid():
            deklaracja = Deklaracja(tematid=student.tematid, studentid= student,
                                    celizakres=form.cleaned_data['goal'],
                                    opis=form.cleaned_data['description'])
            deklaracja.save()
            success = True

        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid,
                             student.deklaracja_set.count())
        context = {'user': student, 'form': form, 'success': success}
        return render(request, 'deklaracja/deklaracja.html', context)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.PowiadomienieOWyborzeTematu import PowiadomienieOWyborzeTematu
from dyplomowanie.model.Student import Student
from .forms import OptionsForm, TopicForm
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO

STUD_ID = 1

class Topics(View):
    """
    Kontroler odpowiadający za widok listy tematów
    Template: widok/tematy/listy_tematow.html
    """
    student = Student.objects.get(id=STUD_ID)

    def post(self, request):
        """
        1) Użytkownik wybrał opcje przeglądania tematów (wówczas temat_wybrany = False),
            zostają wybrane tematy z bazy danych zgodnie z preferencjami użytkownika

        2) Użytkownik wybrał temat, (temat_wybrany = True),
            temat zostaje przypisany użytkownikowi

        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'tematy': tematy - lista obiektów DTO opisujących tematy z bazy danych
                przefiltrowanych zgodnie z preferencjami użytkownika
            'success': success - informacja o tym, czy powiodło się przypisanie użytkownikowi tematu
        :param request:
        :return:
        """
        success = False
        temat_wybrany = True

        form = TopicForm(request.POST)
        if not form.is_valid():
            temat_wybrany = False
            form = OptionsForm(request.POST)
            if not form.is_valid():
                return redirect("topics_options")

        if temat_wybrany:
            temat = Temat.objects.get(id=form.cleaned_data['topic_id'])
            self.student.set_topic(temat)
            temat.make_taken()
            self.make_notification(temat)
            success = True

        filters = {'nauczycielakademickiid__nazwisko__contains': form.cleaned_data['name']}
        if form.cleaned_data['topic_options'] == 'free':
            filters['czywolny'] = 1
        tematy = self.create_DTO_list(Temat.objects.all().filter(**filters))

        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid)
        context = {'user': student_dto, 'tematy': tematy, 'success': success}
        return render(request, 'tematy/listy_tematow.html', context)

    def create_DTO_list(self, tematy):
        result = []
        for temat in tematy:
            status = 'wolny' if temat.czywolny else 'zajęty'
            result.append(TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid), status))
        return result

    def make_notification(self, temat):
        notification = PowiadomienieOWyborzeTematu(
            studentid=self.student,
            tematid=temat,
            nauczycielakademickiid=temat.nauczycielakademickiid)
        notification.save()

class Topics_Options(View):
    """
    Kontroler odpowiadający za widok formularza z opcjami przeglądania tematów
    Template: widok/tematy/opcje_przegladania.html
    """
    student = Student.objects.get(id=STUD_ID)

    def get(self, request):
        """
        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'form': form - wygenerowany formularz (kontroler/forms.py OptionForm)
        :param request:
        :return:
        """

        form = OptionsForm()
        student_dto = StudentDTO(self.student.id, self.student.imie,
                                 self.student.nazwisko, self.student.nrindeksu,
                                 self.student.tematid)
        context = {'user': student_dto, 'form': form}

        return render(request, 'tematy/opcje_przegladania.html', context)
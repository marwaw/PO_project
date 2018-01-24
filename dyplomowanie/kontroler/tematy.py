from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from dyplomowanie.DTO.Student import StudentDTO
from dyplomowanie.model.PowiadomienieOWyborzeTematu import PowiadomienieOWyborzeTematu
from dyplomowanie.model.Student import Student
from .forms import OptionsForm, TopicForm
from dyplomowanie.model.Temat import Temat
from dyplomowanie.DTO.tematy import TematDTO

STUD_ID = 2

class Topics(View):
    """
    Kontroler odpowiadający za widok listy tematów
    Template: widok/tematy/listy_tematow.html
    """

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
        student = Student.objects.get(id=STUD_ID)
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
            self.set_topic_for_student(student, temat)
            self.make_topic_taken(temat)
            self.make_notification(student, temat)
            success = True

        filters = {'nauczycielakademickiid__nazwisko__contains': form.cleaned_data['name']}
        if form.cleaned_data['topic_options'] == 'free':
            filters['czywolny'] = 1
        tematy = self.create_DTO_list(Temat.objects.all().filter(**filters))

        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid)
        context = {'user': student, 'tematy': tematy, 'success': success}
        return render(request, 'tematy/listy_tematow.html', context)

    def create_DTO_list(self, tematy):
        result = []
        for temat in tematy:
            status = 'wolny' if temat.czywolny else 'zajęty'
            result.append(TematDTO(temat.id, temat.trescpl, str(temat.nauczycielakademickiid), status))
        return result

    def set_topic_for_student(self, student, temat):
        student.tematid = temat
        student.save()

    def make_topic_taken(self, temat):
        temat.czywolny = 0
        temat.save()

    def make_notification(self, student, temat):
        notification = PowiadomienieOWyborzeTematu(
            studentid=student,
            tematid=temat,
            nauczycielakademickiid=temat.nauczycielakademickiid)
        notification.save()

class Topics_Options(View):
    """
    Kontroler odpowiadający za widok formularza z opcjami przeglądania tematów
    Template: widok/tematy/opcje_przegladania.html
    """
    def get(self, request):
        """
        context:
            'user': student - obiekt DTO przechowujący najważniejsze dane o studencie
            'form': form - wygenerowany formularz (kontroler/forms.py OptionForm)
        :param request:
        :return:
        """
        student = Student.objects.get(id=STUD_ID)

        form = OptionsForm()
        student = StudentDTO(student.id, student.imie, student.nazwisko, student.nrindeksu, student.tematid)
        context = {'user': student, 'form' : form}

        return render(request, 'tematy/opcje_przegladania.html', context)
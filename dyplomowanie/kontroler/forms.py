from django import forms
from django.forms import ModelForm
from dyplomowanie.model.JezykRealizacji import JezykRealizacji
from dyplomowanie.model import Deklaracja


class OptionsForm(forms.Form):
    """
    Formularz z opcjami przeglądania listy tematów
    TOPIC_CHOICES:
        'wszystkie' - wszystkie tematy (wolne i zajęte)
        'tylko wolne' - tematy, które nie zostały jeszcze wybrane przez żadnego studenta
    name - pole pozwalające filtrować tematy po nazwisku promotora, nie jest wymagane
    topic_options - pole, które jest grupą przycisków pozwalających na wybór tylko jednej z opcji do wyboru (opcje: TOPIC_CHOICES)
    """
    TOPIC_CHOICES = [('all', 'wszystkie'), ('free', 'tylko wolne')]
    name = forms.CharField(label='Nazwisko promotora', max_length=100, required=False)
    topic_options = forms.CharField(label='Jakie tematy wyświetlić?',
                                    widget=forms.RadioSelect(choices=TOPIC_CHOICES), initial='all', required=False)


class DeclarationForm2(forms.Form):
    jezyki = [(jezyk.id, jezyk.nazwajezyka) for jezyk in JezykRealizacji.objects.all()]

    name = forms.CharField(label='Imię')
    surname = forms.CharField(label='Nazwisko')
    subject = forms.CharField(label='Kierunek')
    speciality = forms.CharField(label='Specjalność', required=False)
    studies_more = forms.CharField(label='Stopień, forma i rok studiów')
    topic_PL = forms.CharField(label='Temat PL')
    topic_ENG = forms.CharField(label='Temat ENG')
    supervisor = forms.CharField(label='Opiekun')
    language = forms.ChoiceField(label='Język', choices=jezyki, initial='polski')
    goal = forms.CharField(label='Cel i zakres pracy dyplomowej', widget=forms.Textarea, max_length=2000)
    description = forms.CharField(label='Opis pracy', widget=forms.Textarea, max_length=2000)


class TopicForm(forms.Form):
    topic_id = forms.CharField()
    student_id = forms.CharField()

    TOPIC_CHOICES = [('all', 'wszystkie'), ('free', 'tylko wolne')]
    name = forms.CharField(max_length=100, required=False)
    topic_options = forms.CharField(widget=forms.RadioSelect(choices=TOPIC_CHOICES), initial='all', required=False)

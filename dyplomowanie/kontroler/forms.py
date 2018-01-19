from django import forms

class NameForm(forms.Form):
    TOPIC_CHOICES = [('all', 'wszystkie'), ('free', 'tylko wolne')]
    name = forms.CharField(label = 'Nazwisko promotora', max_length=100)
    topic_options = forms.CharField(label = 'Jakie tematy wyświetlić?',
                                    widget = forms.RadioSelect(choices = TOPIC_CHOICES))

class DeclarationForm(forms.Form):
    name = forms.CharField(label='Imię')
    surname = forms.CharField(label='Nazwisko')
    subject = forms.CharField(label='Kierunek')
    speciality = forms.CharField(label='Specjalność')
    studies_more = forms.CharField(label='Stopień, forma i rok studiów')
    topic_PL = forms.CharField(label='Temat PL')
    topic_ENG = forms.CharField(label='Temat ENG')
    supervisor = forms.CharField(label='Opiekun')
    language = forms.ChoiceField(label='Język', choices = [('polish', 'polski'), ('english', 'angielski')])
    goal = forms.CharField(label = 'Cel i zakres pracy dyplomowej', widget = forms.Textarea, max_length= 2000)
    description = forms.CharField(label = 'Opis pracy', widget = forms.Textarea, max_length= 2000)
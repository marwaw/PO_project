from django.db import models
from django.forms import ModelForm


class Deklaracja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')
    celizakres = models.CharField(db_column='CelIzakres', max_length=2000, blank=True, null=True)
    opis = models.CharField(db_column='Opis', max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'deklaracja'

class DeclarationForm(ModelForm):
    class Meta:
        model = Deklaracja
        fields = ['celizakres', 'opis']

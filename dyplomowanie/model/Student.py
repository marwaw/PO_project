from django.db import models

class Student(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    login = models.CharField(db_column='Login', unique=True, max_length=30)
    haslo = models.CharField(db_column='Haslo', max_length=255)
    imie = models.CharField(db_column='Imie', max_length=255)
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)
    nrindeksu = models.CharField(db_column='NrIndeksu', unique=True, max_length=9)
    kierunekstudiow = models.CharField(db_column='KierunekStudiow', max_length=255)
    specjalnosc = models.CharField(db_column='Specjalnosc', max_length=255, blank=True, null=True)
    rokstudiow = models.IntegerField(db_column='RokStudiow')
    formastudiow = models.ForeignKey('FormaStudiow', models.DO_NOTHING, db_column='FormaStudiow')
    stopienstudiow = models.ForeignKey('StopienStudiow', models.DO_NOTHING, db_column='StopienStudiow')
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'

    def __str__(self):
        return f'{self.imie} {self.nazwisko}, {self.nrindeksu}'

    def set_topic(self, temat):
        self.tematid = temat
        self.save()
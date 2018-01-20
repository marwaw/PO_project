from django.db import models

class NauczycielAkademicki(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    login = models.CharField(db_column='Login', unique=True, max_length=30)
    haslo = models.CharField(db_column='Haslo', max_length=255)
    imie = models.CharField(db_column='Imie', max_length=255)
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)
    sumagodzin = models.IntegerField(db_column='SumaGodzin')

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki'

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
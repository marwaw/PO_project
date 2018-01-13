from django.db import models

class NauczycielAkademicki(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=30)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=255)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=255)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)  # Field name made lowercase.
    sumagodzin = models.IntegerField(db_column='SumaGodzin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki'
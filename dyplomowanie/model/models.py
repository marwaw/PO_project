from django.db import models

class Deklaracja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    celizakres = models.CharField(db_column='CelIzakres', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deklaracja'




class FormaStudiow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwaformy = models.CharField(db_column='nazwaFormy', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formastudiow'


class Jezykrealizacji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwajezyka = models.CharField(db_column='nazwaJezyka', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jezykrealizacji'


class Nauczycielakademicki(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=30)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=255)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=255)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)  # Field name made lowercase.
    sumagodzin = models.IntegerField(db_column='SumaGodzin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nauczycielakademicki'


class Powiadomienieowyborzetematu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')  # Field name made lowercase.
    nauczycielakademickiid = models.ForeignKey(Nauczycielakademicki, models.DO_NOTHING, db_column='NauczycielAkademickiID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'powiadomienieowyborzetematu'


class Stopienstudiow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    stopien = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'stopienstudiow'


class Student(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', unique=True, max_length=30)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=255)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=255)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=255)  # Field name made lowercase.
    nrindeksu = models.CharField(db_column='NrIndeksu', unique=True, max_length=9)  # Field name made lowercase.
    kierunekstudiow = models.CharField(db_column='KierunekStudiow', max_length=255)  # Field name made lowercase.
    specjalnosc = models.CharField(db_column='Specjalnosc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stopienstudiow = models.ForeignKey(Stopienstudiow, models.DO_NOTHING, db_column='StopienStudiow')  # Field name made lowercase.
    formastudiow = models.ForeignKey(FormaStudiow, models.DO_NOTHING, db_column='FormaStudiow')  # Field name made lowercase.
    rokstudiow = models.IntegerField(db_column='RokStudiow')  # Field name made lowercase.
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Temat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    trescpl = models.CharField(db_column='TrescPL', max_length=255)  # Field name made lowercase.
    tresceng = models.CharField(db_column='TrescENG', max_length=255)  # Field name made lowercase.
    nauczycielakademickiid = models.ForeignKey(Nauczycielakademicki, models.DO_NOTHING, db_column='NauczycielAkademickiID')  # Field name made lowercase.
    typ = models.ForeignKey('Typpracy', models.DO_NOTHING, db_column='Typ')  # Field name made lowercase.
    jezykrealizacji = models.ForeignKey(Jezykrealizacji, models.DO_NOTHING, db_column='JezykRealizacji', blank=True, null=True)  # Field name made lowercase.
    maxiloscrealizujacych = models.IntegerField(db_column='MaxIloscRealizujacych')  # Field name made lowercase.
    czyzatwierdzony = models.IntegerField(db_column='CzyZatwierdzony')  # Field name made lowercase.
    czywolny = models.IntegerField(db_column='CzyWolny')  # Field name made lowercase.
    czyzaliczona = models.IntegerField(db_column='CzyZaliczona', blank=True, null=True)  # Field name made lowercase.
    czyplagiat = models.IntegerField(db_column='CzyPlagiat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temat'


class Typpracy(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwatypu = models.CharField(db_column='nazwaTypu', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typpracy'

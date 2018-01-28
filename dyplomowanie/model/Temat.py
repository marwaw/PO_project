from django.db import models

class Temat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    trescpl = models.CharField(db_column='TrescPL', max_length=255)
    tresceng = models.CharField(db_column='TrescENG', max_length=255)
    nauczycielakademickiid = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING, db_column='NauczycielAkademickiID')
    typ = models.ForeignKey('TypPracy', models.DO_NOTHING, db_column='Typ')
    jezykrealizacji = models.ForeignKey('JezykRealizacji', models.DO_NOTHING, db_column='JezykRealizacji', blank=True, null=True)
    maxiloscrealizujacych = models.IntegerField(db_column='MaxIloscRealizujacych')
    czyzatwierdzony = models.IntegerField(db_column='CzyZatwierdzony')
    czywolny = models.IntegerField(db_column='CzyWolny')
    czyzaliczona = models.IntegerField(db_column='CzyZaliczona', blank=True, null=True)
    czyplagiat = models.IntegerField(db_column='CzyPlagiat', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'temat'

    def __str__(self):
        return self.trescpl

    def make_taken(self):
        self.czywolny = 0
        self.save()
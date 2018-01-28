from django.db import models

class Deklaracja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')
    celizakres = models.CharField(db_column='CelIzakres', max_length=2000, blank=True, null=True)
    opis = models.CharField(db_column='Opis', max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'deklaracja'
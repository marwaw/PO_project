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

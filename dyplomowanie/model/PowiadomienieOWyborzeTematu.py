from django.db import models


class PowiadomienieOWyborzeTematu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')
    nauczycielakademickiid = models.ForeignKey('NauczycielAkademicki', models.DO_NOTHING, db_column='NauczycielAkademickiID')

    class Meta:
        managed = False
        db_table = 'powiadomienieowyborzetematu'
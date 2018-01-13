from django.db import models
from dyplomowanie.model import NauczycielAkademicki

class PowiadomienieOWyborzeTematu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentID')  # Field name made lowercase.
    tematid = models.ForeignKey('Temat', models.DO_NOTHING, db_column='TematID')  # Field name made lowercase.
    nauczycielakademickiid = models.ForeignKey(NauczycielAkademicki, models.DO_NOTHING, db_column='NauczycielAkademickiID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'powiadomienieowyborzetematu'
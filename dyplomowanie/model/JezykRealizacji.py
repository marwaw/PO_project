from django.db import models

class JezykRealizacji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwajezyka = models.CharField(db_column='nazwaJezyka', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jezykrealizacji'
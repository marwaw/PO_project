from django.db import models

class JezykRealizacji(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nazwajezyka = models.CharField(db_column='nazwaJezyka', unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'jezykrealizacji'
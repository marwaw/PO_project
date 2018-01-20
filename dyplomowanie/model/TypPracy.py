from django.db import models

class TypPracy(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwatypu = models.CharField(db_column='nazwaTypu', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typpracy'

    def __str__(self):
        return self.nazwatypu
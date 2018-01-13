from django.db import models

class FormaStudiow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nazwaformy = models.CharField(db_column='nazwaFormy', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formastudiow'
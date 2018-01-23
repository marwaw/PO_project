from django.db import models

class FormaStudiow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nazwaformy = models.CharField(db_column='nazwaFormy', unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'formastudiow'

    def __str__(self):
        return self.nazwaformy
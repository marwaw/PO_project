from django.db import models

class StopienStudiow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    stopien = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'stopienstudiow'

    def __str__(self):
        return self.stopien
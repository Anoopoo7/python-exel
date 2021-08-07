from django.db import models

class Dpt_model(models.Model):
    department = models.CharField(max_length= 100)
    faculties = models.CharField(max_length= 225) 

    class Meta:
        db_table = "table_1"
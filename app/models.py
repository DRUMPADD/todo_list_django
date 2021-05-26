from django.db import models

# Create your models here.
class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    desc_task = models.CharField(max_length=255, default='description')
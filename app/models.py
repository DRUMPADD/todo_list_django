from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class register(AbstractUser):
    name = models.CharField(max_length=200, blank=False)
    lName = models.CharField(max_length=200, blank=False)

class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    desc_task = models.CharField(max_length=255, default='description')
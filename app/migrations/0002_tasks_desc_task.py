# Generated by Django 3.1.7 on 2021-05-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='desc_task',
            field=models.CharField(default='description', max_length=255),
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alumno_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='edad',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='carnet',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

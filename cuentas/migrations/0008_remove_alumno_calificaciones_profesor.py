# Generated by Django 4.0.3 on 2022-06-05 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_alumno_calificaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno_calificaciones',
            name='Profesor',
        ),
    ]

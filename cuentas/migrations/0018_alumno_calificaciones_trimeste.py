# Generated by Django 4.0.3 on 2022-06-06 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0017_alter_alumno_calificaciones_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno_calificaciones',
            name='trimeste',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
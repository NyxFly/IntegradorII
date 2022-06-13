# Generated by Django 4.0.3 on 2022-06-06 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0018_alumno_calificaciones_trimeste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno_calificaciones',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cuentas.aula_curso'),
        ),
        migrations.AlterField(
            model_name='aula_curso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.curso'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-09 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0019_alter_alumno_calificaciones_curso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido_m',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_p',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='celular',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='año',
            field=models.CharField(choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='grado',
            field=models.CharField(choices=[('1°', '1°'), ('2°', '2°'), ('3°', '3°'), ('4°', '4°'), ('5°', '5°')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='salon',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='seccion',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.CharField(choices=[('Matematicas', 'Matematicas'), ('Ciencias', 'Ciencias'), ('Humanidades', 'Humanidades')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido_m',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido_p',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.OneToOneField(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='alumno_calificaciones',
            unique_together={('curso', 'trimeste')},
        ),
    ]
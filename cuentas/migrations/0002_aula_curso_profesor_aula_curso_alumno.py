# Generated by Django 4.0.3 on 2022-06-02 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(choices=[('1°', '1°'), ('2°', '2°'), ('3°', '3°'), ('4°', '4°'), ('5°', '5°')], max_length=200, null=True)),
                ('año', models.CharField(choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria')], max_length=200, null=True)),
                ('seccion', models.CharField(max_length=10, null=True)),
                ('salon', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('categoria', models.CharField(choices=[('Matematicas', 'Matematicas'), ('Ciencias', 'Ciencias'), ('Humanidades', 'Humanidades')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('apellido_p', models.CharField(max_length=200, null=True)),
                ('apellido_m', models.CharField(max_length=200, null=True)),
                ('celular', models.CharField(max_length=12, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aula_Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_i', models.TimeField(max_length=10, null=True)),
                ('horario_f', models.TimeField(max_length=10, null=True)),
                ('dia_semana', models.CharField(max_length=12, null=True)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aula', to='cuentas.aula')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuentas.curso')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to='cuentas.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('apellido_p', models.CharField(max_length=200, null=True)),
                ('apellido_m', models.CharField(max_length=200, null=True)),
                ('celular', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('aula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alumnos', to='cuentas.aula')),
                ('email', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

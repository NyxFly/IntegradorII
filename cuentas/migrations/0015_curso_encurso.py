# Generated by Django 4.0.3 on 2022-05-03 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0014_alter_cliente_profile_pic_alter_cliente_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('horario', models.CharField(max_length=200, null=True)),
                ('categoria', models.CharField(choices=[('Matematicas', 'Matematicas'), ('Ciencias', 'Ciencias'), ('Humanidades', 'Humanidades')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuentas.cliente')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cuentas.curso')),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-06-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0009_alter_alumno_calificaciones_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_exam', models.CharField(max_length=20, null=True)),
                ('nota', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='alumno_calificaciones',
            name='notas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.calificaciones'),
        ),
    ]

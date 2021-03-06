# Generated by Django 4.0.3 on 2022-06-05 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_alter_alumno_email_alter_profesor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno_Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.IntegerField(blank=True, null=True)),
                ('Profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notaprofe', to='cuentas.aula_curso')),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.alumno')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notacurso', to='cuentas.aula_curso')),
            ],
        ),
    ]

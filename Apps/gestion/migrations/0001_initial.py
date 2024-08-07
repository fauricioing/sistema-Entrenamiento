# Generated by Django 2.2.14 on 2023-08-16 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=100, verbose_name='apellido del jugador')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre del jugador')),
                ('apellido', models.CharField(max_length=100, verbose_name='apellido del jugador')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('direcion', models.CharField(max_length=100, verbose_name='apellido del jugador')),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Pitcheo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantida', models.IntegerField()),
                ('pro_strik', models.FloatField()),
                ('pro_bola', models.FloatField()),
                ('pro_ponche', models.IntegerField()),
                ('recta', models.IntegerField()),
                ('curva', models.IntegerField()),
                ('cambio', models.IntegerField()),
                ('fecha', models.DateField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Atleta')),
            ],
        ),
        migrations.CreateModel(
            name='CondicioFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField(verbose_name='peso del jugador')),
                ('altura', models.FloatField(verbose_name='altura del jugador')),
                ('tiempo_velocidad', models.FloatField()),
                ('fecha', models.DateField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Atleta')),
            ],
        ),
        migrations.CreateModel(
            name='Bateo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.IntegerField()),
                ('hits', models.IntegerField()),
                ('ponche_batiador', models.IntegerField()),
                ('avg', models.FloatField()),
                ('fecha', models.DateField()),
                ('atleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.Atleta')),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-14 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_fundacion', models.DateField()),
                ('estilo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('instrumento', models.CharField(max_length=200)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica06.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_lanzamiento', models.DateField()),
                ('distribuidora', models.CharField(max_length=200)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica06.Grupo')),
            ],
        ),
    ]

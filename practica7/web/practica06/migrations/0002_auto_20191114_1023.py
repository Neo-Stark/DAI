# Generated by Django 2.2.7 on 2019-11-14 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practica06', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='distribuidora',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='fecha_lanzamiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='musico',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='practica06.Grupo'),
        ),
        migrations.AlterField(
            model_name='musico',
            name='instrumento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practica08', '0004_auto_20191218_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musico',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='musico',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

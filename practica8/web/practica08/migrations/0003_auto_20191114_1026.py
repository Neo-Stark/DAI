# Generated by Django 2.2.7 on 2019-11-14 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practica08', '0002_auto_20191114_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musico',
            name='grupo',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='practica08.Grupo'),
        ),
    ]

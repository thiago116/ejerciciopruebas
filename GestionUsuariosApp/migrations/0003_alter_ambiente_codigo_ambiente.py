# Generated by Django 3.2.4 on 2021-10-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuariosApp', '0002_auto_20211011_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiente',
            name='codigo_ambiente',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]

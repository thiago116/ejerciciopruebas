# Generated by Django 3.2.4 on 2021-10-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ambiente', models.IntegerField(blank=True, null=True)),
                ('nombre_ambiente', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_subambiente', models.IntegerField(unique=True)),
                ('nombre_subambiente', models.CharField(max_length=30)),
                ('ubicacion_subambiente', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]

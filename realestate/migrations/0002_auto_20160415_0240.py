# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='main',
            table='main',
        ),
    ]

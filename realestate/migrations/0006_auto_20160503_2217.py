# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_remove_city_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]

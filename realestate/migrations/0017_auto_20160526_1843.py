# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 18:43
from __future__ import unicode_literals

from django.db import migrations
import realestate.custom_models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0016_auto_20160526_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='main',
            name='price',
            field=realestate.custom_models.CustomMoneyField(),
        ),
    ]

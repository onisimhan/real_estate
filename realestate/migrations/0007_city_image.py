# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_auto_20160503_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
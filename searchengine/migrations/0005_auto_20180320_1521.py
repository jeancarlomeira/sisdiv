# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-20 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0004_auto_20180313_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='name_search',
            field=models.CharField(max_length=500, verbose_name=''),
        ),
    ]

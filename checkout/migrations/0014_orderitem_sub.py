# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-19 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_auto_20180308_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='sub',
            field=models.DecimalField(decimal_places=2, default='0.0', max_digits=8, verbose_name='Sub'),
        ),
    ]

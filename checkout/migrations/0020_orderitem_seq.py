# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_remove_orderitem_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='seq',
            field=models.PositiveIntegerField(default=1, verbose_name='Item'),
        ),
    ]

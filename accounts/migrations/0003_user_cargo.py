# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cargo',
            field=models.CharField(default='', max_length=100, verbose_name='Cargo'),
            preserve_default=False,
        ),
    ]

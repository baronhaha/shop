# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20180206_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='datetime',
        ),
    ]

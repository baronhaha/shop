# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_orderpost_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpost',
            old_name='content',
            new_name='description',
        ),
    ]

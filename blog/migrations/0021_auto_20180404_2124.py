# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory',
            new_name='Category',
        ),
    ]

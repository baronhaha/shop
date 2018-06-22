# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-22 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20180408_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='authorimage',
            field=models.ImageField(default='', upload_to='author_image/'),
            preserve_default=False,
        ),
    ]

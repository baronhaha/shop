# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-23 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180315_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='image',
            field=models.ImageField(default='', upload_to='post_images/'),
            preserve_default=False,
        ),
    ]
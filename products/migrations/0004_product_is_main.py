# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]

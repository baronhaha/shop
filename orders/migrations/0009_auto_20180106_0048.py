# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-05 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orderpost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderpost',
            options={'verbose_name': 'Описание страницы Заказать', 'verbose_name_plural': 'Описание страницы Заказать'},
        ),
    ]

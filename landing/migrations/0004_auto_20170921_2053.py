# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_subscriber_tel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Заказчик', 'verbose_name_plural': 'Мои заказчики'},
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='tel',
            field=models.CharField(default='', max_length=12),
        ),
    ]

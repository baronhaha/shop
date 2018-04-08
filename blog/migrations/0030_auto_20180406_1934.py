# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-06 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20180406_1931'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Транслит'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Категория'),
        ),
        migrations.AlterModelTable(
            name='category',
            table='postcategory',
        ),
    ]

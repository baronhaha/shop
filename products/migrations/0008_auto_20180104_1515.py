# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 12:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171023_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]

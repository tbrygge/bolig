# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0028_auto_20160505_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='kat',
            field=models.CharField(default='medlemsinnlegg', max_length=40),
        ),
    ]

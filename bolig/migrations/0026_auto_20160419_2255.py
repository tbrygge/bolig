# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0025_auto_20160419_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rolle',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0024_auto_20160419_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolle',
            name='logo',
            field=models.FileField(blank=True, max_length=80, null=True, upload_to=''),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0020_linker'),
    ]

    operations = [
        migrations.AddField(
            model_name='linker',
            name='minsak',
            field=models.CharField(default='bullshit', max_length=12),
            preserve_default=False,
        ),
    ]

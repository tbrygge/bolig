# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0015_auto_20160328_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='roller',
            field=models.ManyToManyField(blank=True, to='bolig.Rolle'),
        ),
    ]

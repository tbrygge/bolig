# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0021_linker_minsak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linker',
            name='minsak',
        ),
    ]
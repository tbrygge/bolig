# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0008_remove_person_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='byaddresse',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gateaddresse',
        ),
        migrations.RemoveField(
            model_name='person',
            name='telefon',
        ),
    ]

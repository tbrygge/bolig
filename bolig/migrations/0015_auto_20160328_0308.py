# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0014_person_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='roller',
            field=models.ManyToManyField(blank=True, related_name='persons', to='bolig.Rolle'),
        ),
    ]

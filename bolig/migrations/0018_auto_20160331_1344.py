# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0017_auto_20160328_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leilighet',
            name='personer',
        ),
        migrations.AddField(
            model_name='person',
            name='leilighet',
            field=models.ManyToManyField(blank=True, related_name='leilig', to='bolig.Leilighet'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolig', '0019_rolle_bullshit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True)),
                ('navn', models.CharField(max_length=40)),
                ('type', models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]
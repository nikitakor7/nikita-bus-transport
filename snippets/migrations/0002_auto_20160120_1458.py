# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='time',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='linenos',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

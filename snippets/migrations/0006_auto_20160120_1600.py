# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20160120_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
    ]

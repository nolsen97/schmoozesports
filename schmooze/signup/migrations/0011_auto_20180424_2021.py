# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0010_auto_20180214_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]

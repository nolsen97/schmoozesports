# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20180102_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

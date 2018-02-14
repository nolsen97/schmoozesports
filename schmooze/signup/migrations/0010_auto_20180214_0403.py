# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-14 04:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0009_remove_admin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='admin',
            name='username',
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
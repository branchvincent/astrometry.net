# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-12 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0002_auto_20200729_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_publicly_visible',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1),
        ),
    ]

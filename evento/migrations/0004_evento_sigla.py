# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_auto_20170327_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='sigla',
            field=models.CharField(max_length=200, null=True, verbose_name='nome'),
        ),
    ]

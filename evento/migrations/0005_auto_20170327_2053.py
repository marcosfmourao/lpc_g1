# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_evento_sigla'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='palavrasChave',
            field=models.CharField(max_length=600, null=True, verbose_name='palavras chave'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEHoraDeInicio',
            field=models.DateTimeField(null=True, verbose_name='data e hora de início'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='eventoPrincipal',
            field=models.CharField(max_length=200, null=True, verbose_name='eventoPrincipal'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='sigla',
            field=models.CharField(max_length=200, null=True, verbose_name='sigla'),
        ),
    ]
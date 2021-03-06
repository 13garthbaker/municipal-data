# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-27 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0006_auto_20191127_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='asset_class',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='asset_subclass',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='function',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='iudf',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='ward_location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

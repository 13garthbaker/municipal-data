# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-01 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipal_finance', '0006_auto_20170301_1155'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ageddebtorfacts',
            unique_together=set([('amount_type_code', 'customer_group_code', 'demarcation_code', 'financial_period', 'financial_year', 'item_code', 'period_length'), ('demarcation_code', 'period_code', 'customer_group_code', 'item_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='bsheetfacts',
            unique_together=set([('amount_type_code', 'demarcation_code', 'financial_period', 'financial_year', 'item_code', 'period_length'), ('demarcation_code', 'period_code', 'item_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='capitalfacts',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='incexpfacts',
            unique_together=set([('amount_type_code', 'demarcation_code', 'financial_period', 'financial_year', 'function_code', 'item_code', 'period_length'), ('demarcation_code', 'period_code', 'function_code', 'item_code')]),
        ),
        migrations.AlterUniqueTogether(
            name='repmaintfacts',
            unique_together=set([('amount_type_code', 'demarcation_code', 'financial_period', 'financial_year', 'item_code', 'period_length'), ('demarcation_code', 'period_code', 'item_code')]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-12-11 09:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('municipal_finance', '0034_auto_20201207_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpenditureV2Update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(max_length=255, upload_to='updates/income_expenditure/')),
                ('deleted', models.BigIntegerField(null=True)),
                ('inserted', models.BigIntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'income_expenditure_update',
            },
        ),
        migrations.AlterField(
            model_name='municipalstaffcontactsupdate',
            name='file',
            field=models.FileField(max_length=255, upload_to='updates/municipal_staff_contacts/'),
        ),
    ]

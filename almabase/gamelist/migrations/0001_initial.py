# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=56, null=True)),
                ('platform', models.CharField(blank=True, max_length=16, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('genre', models.CharField(blank=True, max_length=17, null=True)),
                ('editors_choice', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'TABLE 8',
                'managed': False,
            },
        ),
    ]

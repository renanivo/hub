# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import taggit.managers
import utils.softdelete


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=128, verbose_name='nome')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='telefone')),
                ('github_username', models.CharField(blank=True, max_length=50, verbose_name='Github (pessoal)')),
                ('twitter_username', models.CharField(blank=True, max_length=50, verbose_name='Twitter')),
                ('image', models.ImageField(blank=True, help_text='Escolha uma foto real e atual, para que seja identificado - ex.: n\xe3o coloque a foto do Darth Vader. Envie imagens quadradas (m\xednimo 150x150px).', upload_to=b'accounts/', verbose_name='foto')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='e-mail')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='data de anivers\xe1rio')),
                ('starting_date', models.DateField(blank=True, null=True, verbose_name='data de admiss\xe3o')),
                ('leaving_date', models.DateField(blank=True, null=True, verbose_name='data de demiss\xe3o')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CompanyBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='nome')),
            ],
            bases=(models.Model, utils.softdelete.SoftDeleteMixin),
        ),
        migrations.AddField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(max_length=16, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.CompanyBranch', verbose_name='filial'),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='reports_to',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_set', to=settings.AUTH_USER_MODEL, verbose_name='l\xedder direto'),
        ),
        migrations.AddField(
            model_name='account',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
    ]

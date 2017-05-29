# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers
import utils.softdelete


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Changelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_recipients', models.TextField(blank=True, help_text=b'Separe os e-mails por v\xc3\xadrgula', verbose_name='Destinat\xe1rios')),
                ('email_subject', models.CharField(blank=True, help_text='Ex.: "Changelog - Stewie - Sprint 3"', max_length=64, verbose_name='assunto do e-mail')),
                ('description', models.TextField(help_text='Escreva em portugu\xeas. Utilize formata\xe7\xe3o Markdown.', verbose_name='descri\xe7\xe3o')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('email_sent', models.BooleanField(default=False, verbose_name='e-mail enviado')),
                ('last_slack_payload', models.CharField(blank=True, max_length=512, null=True, verbose_name='\xfaltima mensagem para o slack')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_changelogs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=(models.Model, utils.softdelete.SoftDeleteMixin),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='nome')),
                ('headline', models.CharField(blank=True, help_text='Ex.: "Plataforma de recomenda\xe7\xf5es"', max_length=64, verbose_name='headline')),
                ('description', models.TextField(help_text='Utilize formata\xe7\xe3o Markdown', verbose_name='descri\xe7\xe3o')),
                ('repo_id', models.CharField(blank=True, help_text='Inclua a organiza\xe7\xe3o, exemplo: "luizalabs/p36"', max_length=32, verbose_name='reposit\xf3rio Github (org/repo_name)')),
                ('travis_enabled', models.BooleanField(default=False, verbose_name='Incluir badge do Travis CI')),
                ('image', models.ImageField(blank=True, help_text='Todo projeto precisa de um logotipo! Envie imagens quadradas (~500x500px)', upload_to=b'projects/', verbose_name='logotipo')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_projects', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='pessoas que passaram pelo projeto')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='projects.Project', verbose_name=b'Produto')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Team', verbose_name='time mantenedor')),
            ],
            bases=(models.Model, utils.softdelete.SoftDeleteMixin),
        ),
        migrations.AddField(
            model_name='changelog',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]

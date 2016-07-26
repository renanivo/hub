# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PressRelease'
        db.create_table(u'pr_pressrelease', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='added_releases', to=orm['accounts.Account'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'pr', ['PressRelease'])


    def backwards(self, orm):
        # Deleting model 'PressRelease'
        db.delete_table(u'pr_pressrelease')


    models = {
        u'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '128'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'reports_to': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'account_set'", 'null': 'True', 'to': u"orm['accounts.Account']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']", 'null': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'pr.pressrelease': {
            'Meta': {'object_name': 'PressRelease'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'added_releases'", 'to': u"orm['accounts.Account']"}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_set'", 'to': u"orm['accounts.Account']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['pr']
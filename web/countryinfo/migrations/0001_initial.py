# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TransparencyScore'
        db.create_table(u'countryinfo_transparencyscore', (
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'countryinfo', ['TransparencyScore'])


    def backwards(self, orm):
        # Deleting model 'TransparencyScore'
        db.delete_table(u'countryinfo_transparencyscore')


    models = {
        u'countryinfo.transparencyscore': {
            'Meta': {'object_name': 'TransparencyScore'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['countryinfo']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryInfo'
        db.create_table(u'countryinfo_countryinfo', (
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('original_source_name', self.gf('django.db.models.fields.CharField')(max_length=85, blank=True)),
            ('original_source_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('original_source_instructions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('download_filename', self.gf('django.db.models.fields.CharField')(max_length=85, blank=True)),
        ))
        db.send_create_signal(u'countryinfo', ['CountryInfo'])


    def backwards(self, orm):
        # Deleting model 'CountryInfo'
        db.delete_table(u'countryinfo_countryinfo')


    models = {
        u'countryinfo.countryinfo': {
            'Meta': {'object_name': 'CountryInfo'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'download_filename': ('django.db.models.fields.CharField', [], {'max_length': '85', 'blank': 'True'}),
            'original_source_instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'original_source_name': ('django.db.models.fields.CharField', [], {'max_length': '85', 'blank': 'True'}),
            'original_source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'countryinfo.transparencyscore': {
            'Meta': {'object_name': 'TransparencyScore'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['countryinfo']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipient.zipcode'
        db.alter_column(u'data_recipient', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Recipient.zipcode'
        db.alter_column(u'data_recipient', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    models = {
        u'data.countryyear': {
            'Meta': {'ordering': "('year',)", 'object_name': 'CountryYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.datadownload': {
            'Meta': {'object_name': 'DataDownload'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'download_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'data.georecipient': {
            'Meta': {'object_name': 'GeoRecipient'},
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']", 'primary_key': 'True'})
        },
        u'data.location': {
            'Meta': {'ordering': "['path']", 'object_name': 'Location'},
            'average': ('django.db.models.fields.FloatField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'geo_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'recipients': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'data.payment': {
            'Meta': {'object_name': 'Payment'},
            'amounteuro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_index': 'True'}),
            'amountnationalcurrency': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'countrypayment': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4', 'db_index': 'True'}),
            'globalpaymentid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'globalrecipientidx': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'}),
            'paymentid': ('django.db.models.fields.TextField', [], {}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']", 'max_length': '10', 'db_column': "'globalrecipientid'"}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Scheme']", 'db_column': "'globalschemeid'"}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        u'data.recipient': {
            'Meta': {'ordering': "('-total',)", 'object_name': 'Recipient'},
            'address1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'countrypayment': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'countryrecipient': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'geo1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo1nationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo2nationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo3nationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo4': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geo4nationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'globalrecipientid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'globalrecipientidx': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'recipientid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'recipientidx': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_index': 'True'}),
            'town': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'data.recipientschemeyear': {
            'Meta': {'ordering': "('-total',)", 'object_name': 'RecipientSchemeYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Scheme']"}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.recipientyear': {
            'Meta': {'ordering': "('-total',)", 'object_name': 'RecipientYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.scheme': {
            'Meta': {'object_name': 'Scheme'},
            'budgetlines8digit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'countrypayment': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'globalschemeid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'nameenglish': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'namenationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'})
        },
        u'data.schemetype': {
            'Meta': {'object_name': 'SchemeType'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'globalschemeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Scheme']", 'primary_key': 'True'}),
            'scheme_type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'data.schemeyear': {
            'Meta': {'ordering': "('year',)", 'object_name': 'SchemeYear'},
            'countrypayment': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'globalschemeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Scheme']", 'db_column': "'globalschemeid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nameenglish': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.totalyear': {
            'Meta': {'object_name': 'TotalYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']
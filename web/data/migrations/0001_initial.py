# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryYear'
        db.create_table(u'data_countryyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'data', ['CountryYear'])

        # Adding model 'Recipient'
        db.create_table(u'data_recipient', (
            ('recipientid', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('recipientidx', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('globalrecipientid', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('globalrecipientidx', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True)),
            ('address1', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('address2', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('town', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('countryrecipient', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=2, null=True, blank=True)),
            ('countrypayment', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=2, null=True, blank=True)),
            ('geo1', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo2', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo3', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo4', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo1nationallanguage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo2nationallanguage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo3nationallanguage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geo4nationallanguage', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Recipient'])

        # Adding model 'RecipientYear'
        db.create_table(u'data_recipientyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Recipient'])),
            ('name', self.gf('django.db.models.fields.TextField')(null=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'data', ['RecipientYear'])

        # Adding model 'GeoRecipient'
        db.create_table(u'data_georecipient', (
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Recipient'], primary_key=True)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(geography=True)),
        ))
        db.send_create_signal(u'data', ['GeoRecipient'])

        # Adding model 'Payment'
        db.create_table(u'data_payment', (
            ('paymentid', self.gf('django.db.models.fields.TextField')()),
            ('globalpaymentid', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Recipient'], max_length=10, db_column='globalrecipientid')),
            ('globalrecipientidx', self.gf('django.db.models.fields.CharField')(max_length=10, db_index=True)),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Scheme'], db_column='globalschemeid')),
            ('amounteuro', self.gf('django.db.models.fields.FloatField')(null=True, db_index=True)),
            ('amountnationalcurrency', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('countrypayment', self.gf('django.db.models.fields.CharField')(default=None, max_length=4, db_index=True)),
        ))
        db.send_create_signal(u'data', ['Payment'])

        # Adding model 'Scheme'
        db.create_table(u'data_scheme', (
            ('globalschemeid', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('namenationallanguage', self.gf('django.db.models.fields.TextField')(null=True)),
            ('nameenglish', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('budgetlines8digit', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('countrypayment', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'data', ['Scheme'])

        # Adding model 'SchemeYear'
        db.create_table(u'data_schemeyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('globalschemeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Scheme'], db_column='globalschemeid')),
            ('nameenglish', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('countrypayment', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'data', ['SchemeYear'])

        # Adding model 'RecipientSchemeYear'
        db.create_table(u'data_recipientschemeyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Recipient'])),
            ('scheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Scheme'])),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'data', ['RecipientSchemeYear'])

        # Adding model 'SchemeType'
        db.create_table(u'data_schemetype', (
            ('globalschemeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Scheme'], primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('scheme_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'data', ['SchemeType'])

        # Adding model 'TotalYear'
        db.create_table(u'data_totalyear', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Recipient'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')(db_index=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'data', ['TotalYear'])

        # Adding model 'Location'
        db.create_table(u'data_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('geo_type', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('recipients', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')()),
            ('average', self.gf('django.db.models.fields.FloatField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['Location'])

        # Adding model 'DataDownload'
        db.create_table(u'data_datadownload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('download_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['DataDownload'])


    def backwards(self, orm):
        # Deleting model 'CountryYear'
        db.delete_table(u'data_countryyear')

        # Deleting model 'Recipient'
        db.delete_table(u'data_recipient')

        # Deleting model 'RecipientYear'
        db.delete_table(u'data_recipientyear')

        # Deleting model 'GeoRecipient'
        db.delete_table(u'data_georecipient')

        # Deleting model 'Payment'
        db.delete_table(u'data_payment')

        # Deleting model 'Scheme'
        db.delete_table(u'data_scheme')

        # Deleting model 'SchemeYear'
        db.delete_table(u'data_schemeyear')

        # Deleting model 'RecipientSchemeYear'
        db.delete_table(u'data_recipientschemeyear')

        # Deleting model 'SchemeType'
        db.delete_table(u'data_schemetype')

        # Deleting model 'TotalYear'
        db.delete_table(u'data_totalyear')

        # Deleting model 'Location'
        db.delete_table(u'data_location')

        # Deleting model 'DataDownload'
        db.delete_table(u'data_datadownload')


    models = {
        u'data.countryyear': {
            'Meta': {'ordering': "('year',)", 'object_name': 'CountryYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {}),
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
            'total': ('django.db.models.fields.FloatField', [], {}),
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
            'recipientidx': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'total': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'data.recipientschemeyear': {
            'Meta': {'ordering': "('-total',)", 'object_name': 'RecipientSchemeYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'scheme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Scheme']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.recipientyear': {
            'Meta': {'ordering': "('-total',)", 'object_name': 'RecipientYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'total': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.scheme': {
            'Meta': {'object_name': 'Scheme'},
            'budgetlines8digit': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'countrypayment': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'globalschemeid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'nameenglish': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'namenationallanguage': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'total': ('django.db.models.fields.FloatField', [], {})
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
            'total': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.totalyear': {
            'Meta': {'object_name': 'TotalYear'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Recipient']"}),
            'total': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']
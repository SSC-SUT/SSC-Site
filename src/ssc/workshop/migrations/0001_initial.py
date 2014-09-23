# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workshop'
        db.create_table(u'workshop_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('breif_description', self.gf('django.db.models.fields.TextField')()),
            ('full_description', self.gf('django.db.models.fields.TextField')()),
            ('fee', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('length', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'workshop', ['Workshop'])

        # Adding model 'Attendance'
        db.create_table(u'workshop_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workshop.Workshop'])),
            ('date_registered', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('transaction_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('payment', self.gf('django.db.models.fields.IntegerField')()),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'workshop', ['Attendance'])

        # Adding model 'Lecturing'
        db.create_table(u'workshop_lecturing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lecturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workshop.Workshop'])),
            ('payment', self.gf('django.db.models.fields.IntegerField')()),
            ('date_determined', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'workshop', ['Lecturing'])


    def backwards(self, orm):
        # Deleting model 'Workshop'
        db.delete_table(u'workshop_workshop')

        # Deleting model 'Attendance'
        db.delete_table(u'workshop_attendance')

        # Deleting model 'Lecturing'
        db.delete_table(u'workshop_lecturing')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'workshop.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'attendee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date_registered': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment': ('django.db.models.fields.IntegerField', [], {}),
            'transaction_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Workshop']"})
        },
        u'workshop.lecturing': {
            'Meta': {'object_name': 'Lecturing'},
            'date_determined': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'payment': ('django.db.models.fields.IntegerField', [], {}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workshop.Workshop']"})
        },
        u'workshop.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'attended_workshops'", 'null': 'True', 'through': u"orm['workshop.Attendance']", 'to': u"orm['auth.User']"}),
            'breif_description': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fee': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'full_description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lecturers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'lectured_workshops'", 'null': 'True', 'through': u"orm['workshop.Lecturing']", 'to': u"orm['auth.User']"}),
            'length': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['workshop']
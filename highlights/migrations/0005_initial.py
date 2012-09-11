# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HighlightGroup'
        db.create_table('highlights_highlightgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('highlights', ['HighlightGroup'])

        # Adding model 'Highlight'
        db.create_table('highlights_highlight', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('highlight_group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='highlights', to=orm['highlights.HighlightGroup'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('text_button', self.gf('django.db.models.fields.CharField')(default='Read More', max_length=50)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('highlights', ['Highlight'])

    def backwards(self, orm):
        # Deleting model 'HighlightGroup'
        db.delete_table('highlights_highlightgroup')

        # Deleting model 'Highlight'
        db.delete_table('highlights_highlight')

    models = {
        'highlights.highlight': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Highlight'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'highlight_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'highlights'", 'to': "orm['highlights.HighlightGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'text_button': ('django.db.models.fields.CharField', [], {'default': "'Read More'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'highlights.highlightgroup': {
            'Meta': {'object_name': 'HighlightGroup'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['highlights']
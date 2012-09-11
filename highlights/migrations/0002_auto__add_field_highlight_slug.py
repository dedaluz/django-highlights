# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Highlight.slug'
        db.add_column('highlights_highlight', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='default', max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Highlight.slug'
        db.delete_column('highlights_highlight', 'slug')

    models = {
        'highlights.highlight': {
            'Meta': {'ordering': "('position',)", 'object_name': 'Highlight'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'color_button': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'text_button': ('django.db.models.fields.CharField', [], {'default': "'Read More'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['highlights']
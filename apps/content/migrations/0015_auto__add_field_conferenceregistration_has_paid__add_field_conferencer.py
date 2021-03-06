# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ConferenceRegistration.has_paid'
        db.add_column('content_conferenceregistration', 'has_paid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ConferenceRegistration.cost'
        db.add_column('content_conferenceregistration', 'cost',
                      self.gf('django.db.models.fields.FloatField')(default=20),
                      keep_default=False)

        # Adding field 'ConferenceRegistration.pp_token'
        db.add_column('content_conferenceregistration', 'pp_token',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ConferenceRegistration.payer_id'
        db.add_column('content_conferenceregistration', 'payer_id',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ConferenceRegistration.has_paid'
        db.delete_column('content_conferenceregistration', 'has_paid')

        # Deleting field 'ConferenceRegistration.cost'
        db.delete_column('content_conferenceregistration', 'cost')

        # Deleting field 'ConferenceRegistration.pp_token'
        db.delete_column('content_conferenceregistration', 'pp_token')

        # Deleting field 'ConferenceRegistration.payer_id'
        db.delete_column('content_conferenceregistration', 'payer_id')


    models = {
        'content.article': {
            'Meta': {'object_name': 'Article', '_ormbases': ['content.Learn']},
            'article_body': ('django.db.models.fields.TextField', [], {}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'})
        },
        'content.blogcategory': {
            'Meta': {'object_name': 'BlogCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'content.blogentry': {
            'Meta': {'ordering': "['-date']", 'object_name': 'BlogEntry', '_ormbases': ['content.Learn']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['content.BlogCategory']", 'symmetrical': 'False'}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'}),
            'related_songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['content.Song']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'content.church': {
            'Meta': {'object_name': 'Church'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'coords': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'content.conferenceregistration': {
            'Meta': {'object_name': 'ConferenceRegistration'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'church_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'flight_information': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'food_allergies': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'has_paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'housing': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'how_serving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'payer_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'pp_token': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'ride_from_airport': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'}),
            'skills': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_housing_needs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'wanting_to_learn': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'content.contact': {
            'Meta': {'object_name': 'Contact'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'content.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'buy_music_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listed_contributor': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'content.event': {
            'Meta': {'object_name': 'Event'},
            'article_body': ('django.db.models.fields.TextField', [], {}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'content.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        'content.learn': {
            'Meta': {'object_name': 'Learn'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Contributor']"}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'content.listen': {
            'Meta': {'object_name': 'Listen'},
            'album_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'instruments': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'listen_instruments'", 'null': 'True', 'to': "orm['content.Contributor']"}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'record_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'songwriter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listen_songwriter'", 'to': "orm['content.Contributor']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vocals': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'listen_vocals'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['content.Contributor']"})
        },
        'content.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heroshot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heroshots.Image']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        'content.song': {
            'Meta': {'ordering': "['title']", 'object_name': 'Song'},
            'album_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'effective_date': ('django.db.models.fields.DateField', [], {}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Genre']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'instruments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'sont_instruments'", 'null': 'True', 'to': "orm['content.Contributor']"}),
            'lyrics': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'related_articles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['content.Article']", 'null': 'True', 'blank': 'True'}),
            'related_talks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['content.Talk']", 'null': 'True', 'blank': 'True'}),
            'related_videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['content.Watch']", 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'sheet_music': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slides': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'songwriter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Contributor']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vocals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'song_vocals'", 'null': 'True', 'to': "orm['content.Contributor']"})
        },
        'content.talk': {
            'Meta': {'object_name': 'Talk', '_ormbases': ['content.Learn']},
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'content.tutorial': {
            'Meta': {'object_name': 'Tutorial', '_ormbases': ['content.Learn']},
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'}),
            'vimeo_embed_code': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'vimeo_thumb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'vimeo_url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'content.watch': {
            'Meta': {'object_name': 'Watch'},
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vimeo_embed_code': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'vimeo_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'vimeo_thumb': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'vimeo_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'youtube_embed_code': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'youtube_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'heroshots.category': {
            'Meta': {'object_name': 'Category'},
            'crossfade': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'fadetime': ('django.db.models.fields.IntegerField', [], {'default': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'showtime': ('django.db.models.fields.IntegerField', [], {'default': '5', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'heroshots.image': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Image'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heroshots.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['content']
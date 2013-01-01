# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogEntry'
        db.create_table('content_blogentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('content', ['BlogEntry'])

        # Adding M2M table for field related_songs on 'BlogEntry'
        db.create_table('content_blogentry_related_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogentry', models.ForeignKey(orm['content.blogentry'], null=False)),
            ('song', models.ForeignKey(orm['content.song'], null=False))
        ))
        db.create_unique('content_blogentry_related_songs', ['blogentry_id', 'song_id'])

        # Adding field 'Song.genre'
        # db.add_column('content_song', 'genre',
        #               self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
        #               keep_default=False)

        # Adding M2M table for field related_videos on 'Song'
        db.create_table('content_song_related_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['content.song'], null=False)),
            ('watch', models.ForeignKey(orm['content.watch'], null=False))
        ))
        db.create_unique('content_song_related_videos', ['song_id', 'watch_id'])

        # Adding M2M table for field related_articles on 'Song'
        db.create_table('content_song_related_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['content.song'], null=False)),
            ('article', models.ForeignKey(orm['content.article'], null=False))
        ))
        db.create_unique('content_song_related_articles', ['song_id', 'article_id'])

        # Adding M2M table for field related_talks on 'Song'
        db.create_table('content_song_related_talks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['content.song'], null=False)),
            ('talk', models.ForeignKey(orm['content.talk'], null=False))
        ))
        db.create_unique('content_song_related_talks', ['song_id', 'talk_id'])


    def backwards(self, orm):
        # Deleting model 'BlogEntry'
        db.delete_table('content_blogentry')

        # Removing M2M table for field related_songs on 'BlogEntry'
        db.delete_table('content_blogentry_related_songs')

        # Deleting field 'Song.genre'
        #db.delete_column('content_song', 'genre')

        # Removing M2M table for field related_videos on 'Song'
        db.delete_table('content_song_related_videos')

        # Removing M2M table for field related_articles on 'Song'
        db.delete_table('content_song_related_articles')

        # Removing M2M table for field related_talks on 'Song'
        db.delete_table('content_song_related_talks')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'content.article': {
            'Meta': {'object_name': 'Article', '_ormbases': ['content.Learn']},
            'article_body': ('django.db.models.fields.TextField', [], {}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'})
        },
        'content.blogentry': {
            'Meta': {'object_name': 'BlogEntry'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'Meta': {'object_name': 'Song'},
            'album_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            #'genre': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'sont_instruments'", 'null': 'True', 'to': "orm['content.Contributor']"}),
            'lyrics': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'related_articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['content.Article']", 'symmetrical': 'False'}),
            'related_talks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['content.Talk']", 'symmetrical': 'False'}),
            'related_videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['content.Watch']", 'symmetrical': 'False'}),
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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
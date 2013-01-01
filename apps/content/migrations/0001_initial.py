# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Listen'
        db.create_table('content_listen', (
            ('insert_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('producer', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('songwriter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='listen_songwriter', to=orm['content.Contributor'])),
            ('instruments', self.gf('django.db.models.fields.related.ForeignKey')(related_name='listen_instruments', blank=True, null=True, to=orm['content.Contributor'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('mp3', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'])),
            ('album_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('record_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Listen'])

        # Adding M2M table for field vocals on 'Listen'
        db.create_table('content_listen_vocals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('listen', models.ForeignKey(orm['content.listen'], null=False)),
            ('contributor', models.ForeignKey(orm['content.contributor'], null=False))
        ))
        db.create_unique('content_listen_vocals', ['listen_id', 'contributor_id'])

        # Adding model 'Watch'
        db.create_table('content_watch', (
            ('vimeo_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('youtube_embed_code', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('vimeo_thumb', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('vimeo_embed_code', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('insert_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'], null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('youtube_url', self.gf('django.db.models.fields.CharField')(max_length=256, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('vimeo_url', self.gf('django.db.models.fields.CharField')(max_length=256, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Watch'])

        # Adding model 'Learn'
        db.create_table('content_learn', (
            ('insert_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Contributor'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('content', ['Learn'])

        # Adding model 'Tutorial'
        db.create_table('content_tutorial', (
            ('vimeo_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('vimeo_thumb', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('vimeo_embed_code', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('learn_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Learn'], unique=True, primary_key=True)),
            ('vimeo_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('content', ['Tutorial'])

        # Adding model 'Talk'
        db.create_table('content_talk', (
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('learn_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Learn'], unique=True, primary_key=True)),
            ('mp3', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('content', ['Talk'])

        # Adding model 'Article'
        db.create_table('content_article', (
            ('article_body', self.gf('django.db.models.fields.TextField')()),
            ('learn_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['content.Learn'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('content', ['Article'])

        # Adding model 'Song'
        db.create_table('content_song', (
            ('producer', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('lyrics', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('songwriter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Contributor'])),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slides', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('mp3', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'])),
            ('album_title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('sheet_music', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('content', ['Song'])

        # Adding M2M table for field instruments on 'Song'
        db.create_table('content_song_instruments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['content.song'], null=False)),
            ('contributor', models.ForeignKey(orm['content.contributor'], null=False))
        ))
        db.create_unique('content_song_instruments', ['song_id', 'contributor_id'])

        # Adding M2M table for field vocals on 'Song'
        db.create_table('content_song_vocals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['content.song'], null=False)),
            ('contributor', models.ForeignKey(orm['content.contributor'], null=False))
        ))
        db.create_unique('content_song_vocals', ['song_id', 'contributor_id'])

        # Adding model 'Event'
        db.create_table('content_event', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('article_body', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('content', ['Event'])

        # Adding model 'Church'
        db.create_table('content_church', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('coords', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('content', ['Church'])

        # Adding model 'Contributor'
        db.create_table('content_contributor', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('listed_contributor', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('buy_music_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.Church'], null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('content', ['Contributor'])

        # Adding model 'Contact'
        db.create_table('content_contact', (
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('insert_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('content', ['Contact'])

        # Adding model 'Page'
        db.create_table('content_page', (
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('heroshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['heroshots.Image'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('content', ['Page'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Listen'
        db.delete_table('content_listen')

        # Removing M2M table for field vocals on 'Listen'
        db.delete_table('content_listen_vocals')

        # Deleting model 'Watch'
        db.delete_table('content_watch')

        # Deleting model 'Learn'
        db.delete_table('content_learn')

        # Deleting model 'Tutorial'
        db.delete_table('content_tutorial')

        # Deleting model 'Talk'
        db.delete_table('content_talk')

        # Deleting model 'Article'
        db.delete_table('content_article')

        # Deleting model 'Song'
        db.delete_table('content_song')

        # Removing M2M table for field instruments on 'Song'
        db.delete_table('content_song_instruments')

        # Removing M2M table for field vocals on 'Song'
        db.delete_table('content_song_vocals')

        # Deleting model 'Event'
        db.delete_table('content_event')

        # Deleting model 'Church'
        db.delete_table('content_church')

        # Deleting model 'Contributor'
        db.delete_table('content_contributor')

        # Deleting model 'Contact'
        db.delete_table('content_contact')

        # Deleting model 'Page'
        db.delete_table('content_page')
    
    
    models = {
        'content.article': {
            'Meta': {'object_name': 'Article', '_ormbases': ['content.Learn']},
            'article_body': ('django.db.models.fields.TextField', [], {}),
            'learn_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['content.Learn']", 'unique': 'True', 'primary_key': 'True'})
        },
        'content.church': {
            'Meta': {'object_name': 'Church'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'coords': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
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
            'listed_contributor': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'content.listen': {
            'Meta': {'object_name': 'Listen'},
            'album_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'instruments': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listen_instruments'", 'blank': 'True', 'null': 'True', 'to': "orm['content.Contributor']"}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'record_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'songwriter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'listen_songwriter'", 'to': "orm['content.Contributor']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vocals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'listen_vocals'", 'blank': 'True', 'null': 'True', 'to': "orm['content.Contributor']"})
        },
        'content.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heroshot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heroshots.Image']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'content.song': {
            'Meta': {'object_name': 'Song'},
            'album_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Church']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sont_instruments'", 'symmetrical': 'False', 'null': 'True', 'to': "orm['content.Contributor']"}),
            'lyrics': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'sheet_music': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slides': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'songwriter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['content.Contributor']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vocals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'song_vocals'", 'symmetrical': 'False', 'null': 'True', 'to': "orm['content.Contributor']"})
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'heroshots.image': {
            'Meta': {'object_name': 'Image'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['heroshots.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }
    
    complete_apps = ['content']

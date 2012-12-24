from django.db import models
from django.contrib.auth.models import User

from ncfmusic.apps.content.utils import *
import gdata.youtube
import gdata.youtube.service
from gdata.service import RequestError


class Listen(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    mp3 = models.FileField(upload_to='ext/listen')
    songwriter = models.ForeignKey('Contributor', related_name='listen_songwriter')
    producer = models.CharField(max_length=128, null=True, blank=True)
    vocals = models.ManyToManyField('Contributor', null=True, blank=True, related_name='listen_vocals')
    instruments = models.ForeignKey('Contributor', null=True, blank=True, related_name='listen_instruments')
    record_date = models.DateField(null=True, blank=True)
    album_title = models.CharField(max_length=256, null=True, blank=True)
    church = models.ForeignKey('Church')
    insert_date = models.DateField(auto_now_add=True, editable=False)
    source = models.CharField(max_length=1024, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        
def _get_vimeo_json(vimeo_url):
    import re

    m = re.search('/(\d+)$', vimeo_url)
    if m:
        vimeo_id = m.group(1)
        
        api_url = "http://vimeo.com/api/v2/video/%s.json" % vimeo_id
        return _get_vimeo_json_with_api_url(api_url)
        
    
    return '' 

@memoize    
def _get_vimeo_json_with_api_url(api_url):
    import urllib2
    conn = urllib2.Request(url=api_url, headers={'User-Agent' : 'New City Music'})
    
    try:
        f = urllib2.urlopen(conn)
        results = f.read()
    except urllib2.URLError, ue:
        return ''
    
    return results

def _get_embed_code(vimeo_url):
    """
    Figure out the embed code
    """
    
    import simplejson

    objarr = simplejson.loads(_get_vimeo_json(vimeo_url))
    if len(objarr):
        obj = simplejson.loads(_get_vimeo_json(vimeo_url))[0]

        #return '<object width="640" height="360"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=0&amp;show_portrait=0&amp;color=ffffff&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=0&amp;show_portrait=0&amp;color=ffffff&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="640" height="360"></embed></object>' % (obj.get('id'), obj.get('id'))
    
        return '<iframe src="http://player.vimeo.com/video/%s" width="640" height="360" frameborder="0"></iframe>' % obj.get('id')
    else:
        return ''

def _get_vimeo_thumb(vimeo_url):
    import simplejson
    objarr = simplejson.loads(_get_vimeo_json(vimeo_url))
    if len(objarr):
        obj = objarr[0]
        return obj.get('thumbnail_medium')
    else:
        return ''
        
def _get_vimeo_duration(vimeo_url):
    import simplejson
    objarr = simplejson.loads(_get_vimeo_json(vimeo_url))
    if len(objarr):
        obj = objarr[0]
        duration = int(obj.get('duration'))
        return "%d:%d" % (int(duration/60), (duration%60))
    else:
        return ''
        
def _get_vimeo_id(vimeo_url):
    import simplejson
    objarr = simplejson.loads(_get_vimeo_json(vimeo_url))
    if len(objarr):
        obj = objarr[0]
        return obj.get('id')
    else:
        return ''

@memoize
def _get_youtube_id(youtube_url):
    import urlparse

    try:
        return urlparse.parse_qs(urlparse.urlparse(youtube_url).query)['v'][0]
    except:
        return ''

#@memoize
def _get_youtube_data(video_id):
    try:
        yt_service = gdata.youtube.service.YouTubeService()
        return yt_service.GetYouTubeVideoEntry(video_id=video_id)
    except RequestError:
        return None


def _get_youtube_embed(video_id):
    return '<iframe id="player" type="text/html" width="640" height="360" src="http://www.youtube.com/embed/%s?enablejsapi=1&origin=http://ncfmusic.com" frameborder="0"></iframe>' % video_id

def _get_youtube_thumb(video_id):
    entry = _get_youtube_data(video_id)
    if entry:
        return entry.media.thumbnail[0].url

    return ''

def _get_youtube_duration(video_id):
    entry = _get_youtube_data(video_id)
    if entry:
        duration = int(entry.media.duration.seconds)
        return "%d:%d" % (int(duration/60), (duration%60))
    
    return ''

    
class Watch(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True, blank=True)
    church = models.ForeignKey('Church', null=True)
    date = models.DateField(null=True, blank=True)
    vimeo_url = models.CharField(max_length=256, null=True, blank=True, unique=True)
    vimeo_id = models.CharField(max_length=16, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url.")
    vimeo_embed_code = models.CharField(max_length=1024, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url")
    youtube_url = models.CharField(max_length=256, null=True, blank=True, unique=True)
    youtube_id = models.CharField(max_length=16, null=True, blank=True, help_text="If left blank we'll try to figure it out from the YouTube url.")
    youtube_embed_code = models.CharField(max_length=1024, null=True, blank=True, help_text="If left blank we'll try to figure it out from the YouTube url")
    vimeo_thumb = models.CharField(verbose_name='Video Thumb', max_length=256, null=True, blank=True, help_text="If left blank we'll try to figure it out from the Vimeo or YouTube url")
    duration = models.CharField(max_length=16, null=True, blank=True, help_text="If left blank we'll try to figure it out from the Vimeo or YouTube url")
    insert_date = models.DateField(auto_now_add=True, editable=False)
    
    @property
    def embed_code(self):
        if self.vimeo_embed_code:
            return self.vimeo_embed_code
        else:
            return self.youtube_embed_code

    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/watch/%s' % self.slug
        
    class Meta:
        verbose_name_plural = 'Watches'

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.vimeo_url and not self.youtube_url:
            raise ValidationError('You must provide either a Vimeo URL or a YouTube URL.')

        if self.vimeo_url and self.youtube_url:
            raise ValidationError('You cannot have both a Vimeo URL and a YouTube URL.')
        
    def save(self, *args, **kwargs):
        if self.vimeo_url:
            if not self.vimeo_id:
                self.vimeo_id = _get_vimeo_id(self.vimeo_url)
            if not self.vimeo_embed_code:
                self.vimeo_embed_code = _get_embed_code(self.vimeo_url)
            if not self.vimeo_thumb:
                self.vimeo_thumb = _get_vimeo_thumb(self.vimeo_url)
            if not self.duration:
                self.duration = _get_vimeo_duration(self.vimeo_url)
        if self.youtube_url:
            if not self.youtube_id:
                self.youtube_id = _get_youtube_id(self.youtube_url)
            if not self.youtube_embed_code:
                self.youtube_embed_code = _get_youtube_embed(self.youtube_id)
            if not self.vimeo_thumb:
                self.vimeo_thumb = _get_youtube_thumb(self.youtube_id)
            if not self.duration:
                self.duration = _get_youtube_duration(self.youtube_id)
        super(Watch, self).save(*args, **kwargs) # Call the "real" save() method.


class Learn(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    date = models.DateField()
    author = models.ForeignKey('Contributor')
    church = models.ForeignKey('Church')
    teaser = models.TextField()
    insert_date = models.DateField(auto_now_add=True, editable=False)
    
class Tutorial(Learn):
    vimeo_url = models.CharField(max_length=256)
    vimeo_id = models.CharField(max_length=16, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url.")
    vimeo_embed_code = models.CharField(max_length=1024, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url")
    vimeo_thumb = models.CharField(max_length=256, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url")
    duration = models.CharField(max_length=16, null=True, blank=True, help_text="If left blank we'll try to figure it out from the vimeo url")
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/tutorials/%s' % self.slug
        
    def save(self, *args, **kwargs):
        if not self.vimeo_id:
            self.vimeo_id = _get_vimeo_id(self.vimeo_url)
        if not self.vimeo_embed_code:
            self.vimeo_embed_code = _get_embed_code(self.vimeo_url)
        if not self.vimeo_thumb:
            self.vimeo_thumb = _get_vimeo_thumb(self.vimeo_url)
        if not self.duration:
            self.duration = _get_vimeo_duration(self.vimeo_url)
        super(Tutorial, self).save(*args, **kwargs) # Call the "real" save() method.
    
class Talk(Learn):
    duration = models.CharField(max_length=16)
    mp3 = models.FileField(upload_to='ext/talks')
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/talks/%s' % self.slug
    
class Article(Learn):
    article_body = models.TextField()
    
    def __unicode__(self):
        return self.title
        
    def get_absolute_url(self):
        return '/articles/%s' % self.slug
    
class Genre(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

class ResourceManager(models.Manager):
    def get_query_set(self):
        qs = super(ResourceManager, self).get_query_set()

        return sorted(qs.all(), key=lambda s: s.effective_date, reverse=True)


class Song(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    songwriter = models.ForeignKey('Contributor')
    church = models.ForeignKey('Church')
    sheet_music = models.FileField(upload_to='ext/sheet_music', null=True, blank=True)
    slides = models.FileField(upload_to='ext/slides', null=True, blank=True)
    lyrics = models.FileField(upload_to='ext/lyrics', null=True, blank=True)
    producer = models.CharField(max_length=256, null=True, blank=True)
    vocals = models.ManyToManyField('Contributor', null=True, related_name='song_vocals')
    instruments = models.ManyToManyField('Contributor', null=True, related_name='sont_instruments')
    release_date = models.DateField()
    album_title = models.CharField(max_length=256, null=True, blank=True)
    mp3 = models.FileField(upload_to='ext/songs', null=True, blank=True)
    genre = models.ForeignKey('Genre', null=True)
    related_videos = models.ManyToManyField('Watch')
    related_articles = models.ManyToManyField('Article')
    related_talks = models.ManyToManyField('Talk')
    insert_date = models.DateField(auto_now_add=True, editable=False)
    effective_date = models.DateField(editable=False, null=False, blank=False)

    objects = models.Manager()
    effective_objects = ResourceManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/resource/%s/' % self.slug

    def get_effective_date(self):
        dates = [self.insert_date]
        videos = self.related_videos.order_by('-insert_date')
        articles = self.related_articles.order_by('-insert_date')
        talks = self.related_talks.order_by('-insert_date')

        if videos.count():
            dates.append(videos[0].insert_date)
    
        if articles.count():
            dates.append(articles[0].insert_date)

        if talks.count():
            dates.append(talks[0].insert_date)

        return max(dates)
    
    def save(self, *args, **kwargs):
        self.effective_date = self.get_effective_date()
        super(Song, self).save(*args, **kwargs)

class Event(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.CharField(max_length=64)
    church = models.ForeignKey('Church')
    city = models.CharField(max_length=256)
    teaser = models.TextField()
    article_body = models.TextField()
    photo = models.FileField(upload_to='ext/events', null=True, blank=True)

    def __unicode__(self):
        return self.title

    
class Church(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    coords = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Churches'
        
    def get_absolute_url(self):
        return '/churches/%s' % self.slug
    
class Contributor(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=128, null=True, blank=True)
    church = models.ForeignKey('Church', null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    buy_music_url = models.URLField(null=True, blank=True)
    listed_contributor = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return '/musicians/%s' % self.slug
    
class Contact(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email_address = models.EmailField()
    insert_date = models.DateField(auto_now_add=True, editable=False)
    
class Page(models.Model):
    from ncfmusic.apps.heroshots.models import Image
    
    slug = models.SlugField(max_length=255)
    content = models.TextField(blank=True, null=True)
    heroshot = models.ForeignKey(Image, null=True, blank=True)
    
    def __unicode__(self):
        return self.slug
    

class BlogEntry(models.Model):
    entry_date = models.DateTimeField()
    author = models.ForeignKey(User, editable=False)
    related_songs = models.ManyToManyField('Song')
    text = models.TextField()
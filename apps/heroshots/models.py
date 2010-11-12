from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=255,blank=False)
    slug = models.SlugField(max_length=255)
    crossfade = models.NullBooleanField(default=True,blank=True,null=True,help_text="Transition between images on a page?")
    fadetime = models.IntegerField(default=3,blank=True,help_text="How long should the transitions take in seconds?")
    showtime = models.IntegerField(default=5,blank=True,help_text="How long should each image be shown in seconds?")
	
    def __unicode__(self):
        return self.title

    def images(self):
        imgs = Image.objects.filter(category=self)
        if self.crossfade:
            return imgs
        else:
            return [imgs.order_by('?')[0],]

    class Meta:
        verbose_name_plural = 'categories'

class Image(models.Model):
    image = models.ImageField(upload_to='ext/heroshots')
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,blank=False,unique=False)
    url = models.CharField(max_length=255,blank=True)
    sort_order = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return u'%s%s' % (settings.MEDIA_URL,self.image)

    class Meta:
        ordering = ['sort_order',]


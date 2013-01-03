from django.contrib import admin
from django import forms

from ncfmusic.apps.content.models import *

class ListenAdmin(admin.ModelAdmin):
    list_display = ('title', 'album_title', 'songwriter', 'church', 'record_date', )
    list_filter = ('church', 'record_date' )
    search_fields = ('title', 'album_title', )
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Listen, ListenAdmin)

class WatchAdminForm(forms.ModelForm):
    class Meta:
        model = Watch

    def clean_vimeo_url(self):
        return self.cleaned_data['vimeo_url'] or None

    def clean_youtube_url(self):
        return self.cleaned_data['youtube_url'] or None

class WatchAdmin(admin.ModelAdmin):
    form = WatchAdminForm
    list_display = ('title', 'church', 'date', )
    list_filter = ('church', 'date', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]
        
admin.site.register(Watch, WatchAdmin)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'church', )
    list_filter = ('date', 'author', 'church', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]
        
admin.site.register(Tutorial, TutorialAdmin)

class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'church', )
    list_filter = ('date', 'author', 'church', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]
        
admin.site.register(Talk, TalkAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'church', )
    list_filter = ('date', 'author', 'church', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]
    
admin.site.register(Article, ArticleAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album_title', 'songwriter', 'church', 'release_date', )
    list_filter = ('songwriter', 'church', 'release_date', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]
        
admin.site.register(Song, SongAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'church', )
    list_filter = ('start_date', 'church', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Event, EventAdmin)

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', )
    list_filter = ('state', )
    search_fields = ('name', 'city', 'state', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Church, ChurchAdmin)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'church', )
    list_filter = ('church', )
    search_fields = ('name', 'title', )
    prepopulated_fields = {'slug': ('name',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]

admin.site.register(Contributor, ContributorAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', )
    search_fields = ('first_name', 'last_name', 'email_address', )
    
admin.site.register(Contact, ContactAdmin)

admin.site.register(Page)

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Genre, GenreAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(BlogCategory, BlogCategoryAdmin)


class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}
    
    class Media:
        js = [
            '/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', 
            '/media/admin/tinymce_setup/tinymce_setup.js',
        ]

    def save_model(self, request, obj, form, change):
        try:
            author = obj.author
        except User.DoesNotExist:
            obj.author = request.user
        
        obj.save()

admin.site.register(BlogEntry, BlogEntryAdmin)
        
        
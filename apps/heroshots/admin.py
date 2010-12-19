from django.contrib import admin
from ncfmusic.apps.heroshots.models import Image, Category

class ImageInline(admin.TabularInline):
	model = Image
    # exclude = ('sort_order',)
	extra = 1
	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ('title',)}
	exclude = ('crossfade', 'fadetime', 'showtime',)
	inlines = [
		ImageInline,
	]

admin.site.register(Category,CategoryAdmin)
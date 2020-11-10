# Register your models here.
from django.contrib import admin
from .models import Blog
from .models import Album
from .models import Gallery


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)


class AlbumAdmin(admin.ModelAdmin):
    # fields = ['name', 'slug']
    list_display = ('name', 'slug', 'pic')


admin.site.register(Album, AlbumAdmin)


# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('album', 'pic')


# admin.site.register(Gallery, GalleryAdmin)

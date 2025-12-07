from django.contrib import admin
from .models import Studio, Genre, Tag



@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ('name', 'country')
    list_editable = ('country',)
    list_filter = ('name', 'country')
    list_per_page = 25



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ("name", "slug")
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    list_per_page = 25


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ("name", "slug")
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')
    list_per_page = 25
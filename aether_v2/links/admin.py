from django.contrib import admin
from .models import Link, LinkCategory

@admin.register(LinkCategory)
class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'order']
    list_editable = ['order']

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']
    list_filter = ['category']

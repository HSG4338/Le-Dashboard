from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Appearance', {'fields': ['wallpaper', 'overlay_opacity']}),
        ('Identity', {'fields': ['site_title', 'tagline']}),
        ('Social', {'fields': ['github_url', 'twitter_url', 'email']}),
    ]

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

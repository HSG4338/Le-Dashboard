from django.db import models


class SiteSettings(models.Model):
    wallpaper = models.ImageField(upload_to='wallpapers/', blank=True, null=True)
    overlay_opacity = models.FloatField(default=0.7)
    site_title = models.CharField(max_length=100, default='Aether')
    tagline = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        from django.core.cache import cache
        cache.delete('site_settings')

    @classmethod
    def get(cls):
        from django.core.cache import cache
        obj = cache.get('site_settings')
        if obj is None:
            obj, _ = cls.objects.get_or_create(pk=1)
            cache.set('site_settings', obj, 3600)
        return obj

from django.db import models


class LinkCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=10, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Link Categories'

    def __str__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.ForeignKey(LinkCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='links')
    description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

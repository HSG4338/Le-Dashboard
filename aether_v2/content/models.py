from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from django.db import models


class NewsIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel('intro')]
    subpage_types = ['content.NewsPage']

    def get_context(self, request):
        ctx = super().get_context(request)
        ctx['posts'] = self.get_children().live().order_by('-first_published_at')
        return ctx


class NewsPage(Page):
    summary = models.CharField(max_length=300, blank=True)
    body = RichTextField()
    search_fields = Page.search_fields + [index.SearchField('body')]
    content_panels = Page.content_panels + [FieldPanel('summary'), FieldPanel('body')]
    parent_page_types = ['content.NewsIndexPage']
    subpage_types = []


class VlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel('intro')]
    subpage_types = ['content.VlogPage']

    def get_context(self, request):
        ctx = super().get_context(request)
        ctx['entries'] = self.get_children().live().order_by('-first_published_at')
        return ctx


class VlogPage(Page):
    video_url = models.URLField()
    description = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel('video_url'), FieldPanel('description')]
    parent_page_types = ['content.VlogIndexPage']
    subpage_types = []


class NowPage(Page):
    body = RichTextField()
    updated_note = models.CharField(max_length=200, blank=True)
    content_panels = Page.content_panels + [FieldPanel('updated_note'), FieldPanel('body')]
    max_count = 1
    subpage_types = []

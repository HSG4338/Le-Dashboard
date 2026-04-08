from django.apps import AppConfig


class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'

    def ready(self):
        from wagtail.signals import page_published

        def on_page_published(sender, instance, **kwargs):
            from activity.models import ActivityLog
            ActivityLog.objects.create(
                action_type='content_published',
                description=f'Published: "{instance.title}" ({instance.__class__.__name__})',
            )

        page_published.connect(on_page_published, weak=False)

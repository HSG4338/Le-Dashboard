from django.apps import AppConfig


class ActivityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activity'

    def ready(self):
        # Wire up signals — all imports happen inside the function, after all apps are loaded
        from django.db.models.signals import post_save

        def log_project(sender, instance, created, **kwargs):
            from activity.models import ActivityLog
            ActivityLog.objects.create(
                action_type='project_created' if created else 'project_updated',
                description=f'{"Created" if created else "Updated"}: "{instance.title}" [{instance.get_status_display()}]',
            )

        def log_suggestion(sender, instance, created, **kwargs):
            if not created:
                return
            from activity.models import ActivityLog
            ActivityLog.objects.create(
                action_type='suggestion_received',
                description=f'New suggestion from {instance.name or "Anonymous"}',
            )

        def log_link(sender, instance, created, **kwargs):
            if not created:
                return
            from activity.models import ActivityLog
            ActivityLog.objects.create(
                action_type='link_added',
                description=f'New link added: "{instance.title}"',
            )

        from projects.models import Project
        from suggestions.models import Suggestion
        from links.models import Link

        post_save.connect(log_project, sender=Project, weak=False)
        post_save.connect(log_suggestion, sender=Suggestion, weak=False)
        post_save.connect(log_link, sender=Link, weak=False)

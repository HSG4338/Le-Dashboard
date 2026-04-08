from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **options):
        from projects.models import Project, Tag
        from links.models import Link, LinkCategory
        from site_settings.models import SiteSettings

        s = SiteSettings.get()
        s.site_title = 'Aether'
        s.tagline = 'Developer. Builder. Thinker. This is my corner of the internet.'
        s.github_url = 'https://github.com'
        s.email = 'hello@example.com'
        s.save()

        tag_names = ['Python', 'Django', 'React', 'TypeScript', 'Rust', 'AI/ML', 'DevOps', 'Design']
        tags = {}
        for name in tag_names:
            t, _ = Tag.objects.get_or_create(name=name)
            tags[name] = t

        projects = [
            ('Aether Hub', 'Personal web hub built with Django and Wagtail. Frosted glass UI, activity logging, full admin.', 'shipped', 'https://github.com', '', ['Python', 'Django', 'Design']),
            ('Neural Canvas', 'AI-powered image generation interface with prompt management and style presets.', 'building', 'https://github.com', '', ['Python', 'AI/ML', 'React']),
            ('Ripple CLI', 'Fast dotfile syncing across machines. Zero dependencies, Rust-native, works on Mac and Linux.', 'shipped', 'https://github.com', '', ['Rust', 'DevOps']),
            ('Tempo', 'Distraction-free writing environment with Pomodoro timer and local-first storage.', 'paused', '', '', ['TypeScript', 'Design']),
            ('Keystone', 'Minimal secrets manager for small teams. Encrypts env vars and syncs to S3.', 'building', 'https://github.com', '', ['Python', 'DevOps']),
        ]
        for title, desc, status, repo, live, tag_list in projects:
            p, created = Project.objects.get_or_create(title=title, defaults={'description': desc, 'status': status, 'repo_url': repo, 'live_url': live})
            if created:
                for t in tag_list:
                    p.tags.add(tags[t])

        cats = {}
        for name, icon in [('Tools', ''), ('Reading', ''), ('Design', ''), ('Dev Resources', '')]:
            c, _ = LinkCategory.objects.get_or_create(name=name, defaults={'icon': icon})
            cats[name] = c

        links = [
            ('Linear', 'https://linear.app', 'Tools', 'Issue tracking that feels good'),
            ('Raycast', 'https://raycast.com', 'Tools', 'Mac launcher, supercharged'),
            ('Hacker News', 'https://news.ycombinator.com', 'Reading', 'Tech news, daily'),
            ('Dribbble', 'https://dribbble.com', 'Design', 'Design inspiration'),
            ('Coolors', 'https://coolors.co', 'Design', 'Colour palette generator'),
            ('Django Docs', 'https://docs.djangoproject.com', 'Dev Resources', 'The reference'),
            ('MDN Web Docs', 'https://developer.mozilla.org', 'Dev Resources', 'Web platform docs'),
        ]
        for title, url, cat, desc in links:
            Link.objects.get_or_create(title=title, defaults={'url': url, 'category': cats[cat], 'description': desc})

        self.stdout.write(self.style.SUCCESS('Database seeded. Run: python manage.py createsuperuser'))

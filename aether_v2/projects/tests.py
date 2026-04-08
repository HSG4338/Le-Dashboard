from django.test import TestCase
from projects.models import Project, Tag
from suggestions.forms import SuggestionForm
from suggestions.models import Suggestion


class TagTests(TestCase):
    def test_slug_auto_generated(self):
        t = Tag.objects.create(name='Machine Learning')
        self.assertEqual(t.slug, 'machine-learning')

    def test_str(self):
        t = Tag.objects.create(name='Python')
        self.assertEqual(str(t), 'Python')


class ProjectTests(TestCase):
    def test_slug_auto_generated(self):
        p = Project.objects.create(title='My Cool App', description='desc')
        self.assertEqual(p.slug, 'my-cool-app')

    def test_default_status_building(self):
        p = Project.objects.create(title='Test', description='desc')
        self.assertEqual(p.status, 'building')

    def test_str(self):
        p = Project.objects.create(title='Hello', description='desc')
        self.assertEqual(str(p), 'Hello')


class ProjectViewTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title='Test Project', description='A test project for views')

    def test_home_200(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_list_200(self):
        r = self.client.get('/projects/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Test Project')

    def test_detail_200(self):
        r = self.client.get(f'/projects/{self.project.slug}/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Test Project')

    def test_filter_status(self):
        r = self.client.get('/projects/?status=building')
        self.assertEqual(r.status_code, 200)

    def test_htmx_partial(self):
        r = self.client.get('/projects/', HTTP_HX_REQUEST='true')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'projects/_grid.html')

    def test_404(self):
        r = self.client.get('/projects/nonexistent-slug/')
        self.assertEqual(r.status_code, 404)


class SuggestionFormTests(TestCase):
    def test_valid(self):
        f = SuggestionForm(data={'name': 'Alice', 'message': 'This is a great site!'})
        self.assertTrue(f.is_valid())

    def test_message_too_short(self):
        f = SuggestionForm(data={'name': '', 'message': 'Hi'})
        self.assertFalse(f.is_valid())
        self.assertIn('message', f.errors)

    def test_name_optional(self):
        f = SuggestionForm(data={'name': '', 'message': 'Long enough message here.'})
        self.assertTrue(f.is_valid())

    def test_message_required(self):
        f = SuggestionForm(data={'name': 'Alice', 'message': ''})
        self.assertFalse(f.is_valid())


class SuggestionViewTests(TestCase):
    def test_get(self):
        r = self.client.get('/suggestions/')
        self.assertEqual(r.status_code, 200)

    def test_post_valid(self):
        r = self.client.post('/suggestions/', {'name': 'Test', 'message': 'A valid suggestion message.'})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(Suggestion.objects.count(), 1)

    def test_post_invalid(self):
        r = self.client.post('/suggestions/', {'message': 'short'})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(Suggestion.objects.count(), 0)


class LinksViewTests(TestCase):
    def test_links_200(self):
        r = self.client.get('/links/')
        self.assertEqual(r.status_code, 200)


class ActivityViewTests(TestCase):
    def test_activity_200(self):
        r = self.client.get('/activity/')
        self.assertEqual(r.status_code, 200)

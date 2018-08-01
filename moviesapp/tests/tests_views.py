from django.test import TestCase
# from moviesapp.models import Movie
from django.urls import reverse


class MovieListView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/movies/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('movies:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('movies:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/index.html')

    def test_view_url_exists_at_desired_location_moviedetail(self):
        resp = self.client.get('/movies/1')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_moviedetail(self):
        resp = self.client.get(reverse('movies:detail',
                                       kwargs={'slug': 'bahubali'}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_moviedetail(self):
        resp = self.client.get(reverse('movies:detail',
                               kwargs={'slug': 'bahubali'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'movies/detail.html')

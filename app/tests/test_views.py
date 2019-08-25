from django.http import HttpRequest
from django.test import SimpleTestCase, TransactionTestCase
from django.urls import reverse


class StaticPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_contribute_page_status_code(self):
        response = self.client.get('/contribute/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_api_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)


class DynamicPageTests(TransactionTestCase):

    def test_latest_page_status_code(self):
        response = self.client.get('/latest/')
        self.assertEquals(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)
from django.test import SimpleTestCase, TransactionTestCase


class StaticPageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_api_page_status_code(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_contribute_page_status_code(self):
        response = self.client.get('/contribute/')
        self.assertEquals(response.status_code, 200)


class DynamicPageTests(TransactionTestCase):

    def test_latest_page_status_code(self):
        response = self.client.get('/latest/')
        self.assertEquals(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)


class TestTemplateNames(TransactionTestCase):

    def test_home_page_name(self):
        response = self.client.get('/')
        self.assertTemplateUsed(template_name='home.html')

    def test_api_page_name(self):
        response = self.client.get('/api/')
        self.assertTemplateUsed(template_name='api.html')

    def test_about_page_name(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(template_name='about.html')

    def test_contribute_page_name(self):
        response = self.client.get('/contribute/')
        self.assertTemplateUsed(template_name='contribute.html')

    def test_latest_page_name(self):
        response = self.client.get('/latest/')
        self.assertTemplateUsed(template_name='latest.html')

    def test_tags_page_name(self):
        response = self.client.get('/tags/')
        self.assertTemplateUsed(template_name='tags.html')

# class SearchQueryTests(Test)
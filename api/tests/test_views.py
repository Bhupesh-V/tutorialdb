from django.test import TransactionTestCase


class APITests(TransactionTestCase):

    def test_tutorials_page_status_code(self):
        response = self.client.get('/api/tutorials/')
        self.assertEquals(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/api/tags/')
        self.assertEquals(response.status_code, 200)

    def test_latest_page_status_code(self):
        response = self.client.get('/api/latest/')
        self.assertEquals(response.status_code, 200)

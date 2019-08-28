from django.test import TransactionTestCase


class APITests(TransactionTestCase):

    def test_tutorials_page_status_code(self):
        response = self.client.get('/tutorials')
        self.assertEquals(response.status_code, 200)

    def test_tags_page_status_code(self):
        response = self.client.get('/tags/')
        self.assertEquals(response.status_code, 200)

    def test_latest_page_status_code(self):
        response = self.client.get('/latest/')
        self.assertEquals(response.status_code, 200)

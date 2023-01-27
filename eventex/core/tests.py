from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
        self.html = self.response.content.decode('utf-8')

    def test_get(self):
        """GET / must return code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscribe_link(self):
        """Must contain subscribe link"""
        self.assertContains(self.response, 'href="/inscricao/"')

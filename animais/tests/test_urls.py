from django.test import TestCase
from django.test import RequestFactory


from animais.views import index


class AnimaisUrlsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_url_index(self):
        """Teste se a home utiliza a função index da view"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

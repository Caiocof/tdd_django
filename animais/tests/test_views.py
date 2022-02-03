from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    # def test_index_retorno_animal(self):
    #     """Teste para verificar o retorno das caracteristicas do animal"""
    #     response = self.client.get('/',
    #                                {'caracteristicas': 'resultado'})
    #
    #     self.assertIn(type(response.context['caracteristicas']), QuerySet)

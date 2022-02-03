from django.test import TestCase, RequestFactory

from animais.models import Animal


class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome='Leão',
            predador=True,
            venenoso=False,
            domestico=False
        )

    def test_animal_cadastrado(self):
        """Teste para verificar se o animal esta cadastrado com suas caracteristicas"""
        self.assertEqual(self.animal.nome, 'Leão')

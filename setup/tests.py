from django.test import LiveServerTestCase

import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_busca_animal(self):
        """Test para verificar a usabilidade de buscar animais"""
        self.browser.get(self.live_server_url + '/')

        # Busca por "Busca Animal" no menu
        element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', element.text)

        # Busca o input de "pesquisa animal pelo nome"
        busca_animal = self.browser.find_element(By.ID, 'busca_animal')
        self.assertEqual(busca_animal.get_attribute('placeholder'), 'Ex: Leão')

        # Presence o campo de busca e clica em pesquisar
        busca_animal.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # Mostra 4 caracteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

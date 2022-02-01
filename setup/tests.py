from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('E:\Projetos\TEST-AUTOMATIZADO\\tdd_django\chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_busca_animal(self):
        """Test para verificar a usabilidade de buscar animais"""
        driver = self.browser.get(self.live_server_url + '/')

        # Busca por "Busca Animal" no menu
        element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', element.text)

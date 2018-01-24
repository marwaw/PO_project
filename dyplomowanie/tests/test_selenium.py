import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dyplomowanie.model.Student import Student
from dyplomowanie.model.Temat import Temat
from dyplomowanie.kontroler.tematy import Topics


class DyplomowanieTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\gecko\geckodriver.exe')


    def test_zalogowany(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        self.assertIn("Zalogowany jako", driver.page_source)

    def test_filtr_promotorow(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        driver.find_element_by_id("przegladaj").click()
        driver.find_element_by_id('name').send_keys('Kowal')
        driver.find_element_by_id('szukaj').click()

        self.assertIn("Kowalski", driver.page_source)
        self.assertIn("Kowalska", driver.page_source)

    def tearDown(self):
        self.driver.close()
import unittest

from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dyplomowanie.model.Student import Student
from dyplomowanie.model.Temat import Temat
from dyplomowanie.kontroler.tematy import Topics

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/home/widelec/Projects/fork/geckodriver')
                                        # ścieżka do pliku np: C:\Martyna\geck\geckodriver.exe
    def test_zalogowany(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000") # można użyć adresu dyplomowanie.herok[...], ale muszą być tam zdeployowane zmiany w templatkach
        self.assertIn("Zalogowany jako", driver.page_source)


    def test_informacja_o_braku_wyboru(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        elem = driver.find_element_by_id("praca")
        elem.click()
        self.assertIn("Nie wybrano jeszcze tematu", driver.page_source)

    def test_filtr_promotorow(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        driver.find_element_by_id("przegladaj").click()
        driver.find_element_by_name('name').send_keys('Kowal')
        driver.find_element_by_id('szukaj').click()

        self.assertIn("Kowalski", driver.page_source)
        self.assertIn("Kowalska", driver.page_source)

    def tearDown(self):
        self.driver.close()


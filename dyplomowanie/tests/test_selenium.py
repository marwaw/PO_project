import unittest

from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\gecko\geckodriver.exe')

    def test_zalogowany(self):
        driver = self.driver
        driver.get("https://dyplomowanie.herokuapp.com")
        self.assertIn("Zalogowany jako", driver.page_source)

    def test_informacja_o_wyborze(self):
        driver = self.driver
        driver.get("https://dyplomowanie.herokuapp.com")
        elem = driver.find_element_by_id("praca")
        elem.click()
        self.assertIn("Temat pracy dyplomowej", driver.page_source)

    def test_filtr_promotorow(self):
        driver = self.driver
        driver.get("https://dyplomowanie.herokuapp.com")
        driver.find_element_by_id("przegladaj").click()
        driver.find_element_by_name('name').send_keys('Kowal')
        driver.find_element_by_id('szukaj').click()

        self.assertIn("Kowalski", driver.page_source)
        self.assertIn("Kowalska", driver.page_source)

    def tearDown(self):
        self.driver.close()

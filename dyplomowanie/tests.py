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
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


import unittest
from selenium import webdriver
from pages_.mainPage import MainPage

class ServiceSelection(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://menu.am/en")

    def test_valid_service_selection(self):
        mainPageObject = MainPage(self.driver)
        mainPageObject.

    def tearDown(self):
        self.driver.close()
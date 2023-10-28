import unittest
from selenium import webdriver
from pages_.mainPage import MainPage

class Filters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://menu.am/en")

    def test_filter_selection(self):
        mainPageObject = MainPage(self.driver)
        mainPageObject.click_to_filters_checkbox()

    def tearDown(self):
        self.driver.close()
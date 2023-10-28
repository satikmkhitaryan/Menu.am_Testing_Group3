import unittest
from selenium import webdriver
from pages_.mainPage import MainPage

class SearchBox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://menu.am/en")

    def test_valid_search_box(self):
        mainPageObject = MainPage(self.driver)
        mainPageObject.fill_search_field("pizza")
        mainPageObject.click_to_search_button()

    def tearDown(self):
        self.driver.close()
import unittest
from selenium import webdriver
from pages_.mainPage import MainPage

class ServiceSelection(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://menu.am/en")

    def test_valid_shop_selection(self):
        mainPageObject = MainPage(self.driver)
        if mainPageObject._get_title(self.driver) != "Order food delivery from restaurants 24 Hours - Menu.am":
            print("Error: Wrong page title")
            exit(2)
        mainPageObject.click_to_shop()

    def tearDown(self):
        self.driver.close()
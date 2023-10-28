import unittest
from selenium import webdriver
from pages_.navigationBar import NavigationBar
import time

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://menu.am/en")

    def test_navigation_bar(self):
        navigationBarObj= NavigationBar(self.driver)
        navigationBarObj.click_to_go_to_homepage_button()
        navigationBarObj.click_to_Enter_Your_address_button()
        navigationBarObj.fill_Enter_Your_address_field()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

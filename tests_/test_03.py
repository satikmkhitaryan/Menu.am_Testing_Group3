import unittest
from selenium import webdriver
from pages_.mainPage import MainPage
from pages_.searchResulstPage import SearchResultsPage
from pages_.productDetailsPage import ProductDetailsPage

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://menu.am/en")
        mainPageObject = MainPage(self.driver)
        mainPageObject.fill_search_field("pizza")
        mainPageObject.click_to_search_button()

    def test_valid_search_box(self):
        searchResultsPageObj = SearchResultsPage(self.driver)
        searchResultsPageObj.fill_search_field(" Bruschetta 33cm")
        # searchResultsPageObj.validate_search_button_text()
        searchResultsPageObj.click_to_search_button_element()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.add_to_cart_button()

    def tearDown(self):
        self.driver.close()
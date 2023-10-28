from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def add_to_cart_button(self):
        cartButtonElement = self._find_element(By.XPATH, "//span[contains(text(), 'Add to Cart')]")
        self._click(cartButtonElement)
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class MainPage(BasePage):
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_to_search_field(self):
        searchField = self._find_element(By.NAME, "search")
        self._click(searchField)

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(By.NAME, "search")
        self._click(searchFieldElement)
        self._fill_field(searchFieldElement, text)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(By.XPATH, "(//span[@class='MuiButton-label'])[5]")
        self._click(searchButtonElement)

    def click_to_shop(self):
        serviceElement = self._find_element(By.CSS_SELECTOR, "[title='Muchacho']")
        self._click(serviceElement)

    def click_to_filters_checkbox(self):
        filterCheckboxElement = self._find_element(By.XPATH, "//input[@class='jss1702'][1]")





from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_search_field(self, text):
        searchFieldElement = self._find_element(By.NAME, "search")
        self._fill_field(searchFieldElement, text)

    def click_to_search_button_element(self):
        searchButtonElement = self._find_element(By.XPATH, "//span[contains(text(), 'Search')]")
        self._click(searchButtonElement)

    def click_to_first_product(self):
        firstProductElement = self._find_element(By.XPATH, "(//img[@class='MuiCardMedia-root jss2591 MuiCardMedia-media MuiCardMedia-img'])[1]")

    def validate_search_button_text(self):
        searchButtonElement = self._find_element(By.XPATH, "(//span[@class='MuiButton-label'])[4]")
        if self._get_element_text(searchButtonElement) != "Search":
            print("ERROR: Wrong search button text")
            exit(4)

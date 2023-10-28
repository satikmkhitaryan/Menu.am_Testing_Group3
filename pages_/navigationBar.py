from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_to_go_to_homepage_button(self):
        goToHomepageButton = self._find_element(By.CLASS_NAME,"MuiBox-root jss21")
        self._click(goToHomepageButton)

    def click_to_Enter_Your_address_button(self):
        EnterYouraddressbuttonElement= self._find_element(By.NAME, "set-address")
        self._click(EnterYouraddressbuttonElement)

    def fill_Enter_Your_address_field(self):
        adressSearchFieldElement= self._find_element(By.NAME, "set-address")
        self._fill_field(adressSearchFieldElement,"Azatutyun")

    def click_to_Signin_button(self):
        signinButtonElement= self._find_element(By.XPATH, "(//span[@class='MuiButton-label'])[1])")
        self._click(signinButtonElement)

    def click_to_Signup_button(self):
        signupButtonElement= self._find_element(By.XPATH, "(//span[@class='MuiButton-label'])[2])")
        self._click(signupButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(By.CLASS_NAME, "MuiButtonBase-root MuiButton-root jss34 MuiButton-contained jss1710 MuiButton-containedPrimary jss35 MuiButton-disableElevation")
        self._click(cartButtonElement)

    def validate_count_of_products_in_cart(self):
        cartButtonElement = self._find_element(By.CLASS_NAME, "jss3309")
        self._get_element_text(cartButtonElement)

    def click_language_buttom(self):
        languageButtonElement= self._find_element(By.XPATH, "(//span[@class='MuiButton-label'])[5])")
        self._click(languageButtonElement)
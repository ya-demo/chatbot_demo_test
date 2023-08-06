from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PricingPage(BasePage):

    # Locators
    h1_pricing_title = (By.XPATH, "//h1[text()='Goal-oriented pricing that scales with you']")

    # Actions
    def is_pricing_page(self):
        return self.wait_url_changed("/pricing/")

    def has_pricing_title(self):
        return self.has_element(self.h1_pricing_title, 2)

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    # Locators
    btn_menu_root_pricing = (By.XPATH, "//li[@data-target='menu.root']/a[@href='/pricing/']")

    # Actions
    def to_pricing_page(self, text):
        self.click(self.btn_menu_root_pricing)
        return self

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ChatbotChatFrame(BasePage):

    # Locators
    btn_chatbot_icon = (By.XPATH, "//div[@class='bubble']")
    btn_have_questions = (By.XPATH, "//span[contains(text(), 'I have questions')]")
    btn_menu_pricing = (By.XPATH, "//span[contains(text(), 'Pricing')]")
    btn_compare_plans = (By.XPATH, "//div[contains(text(), 'Compare plans')]")

    # Actions
    def click_chatbot_icon(self):
        self.click(self.btn_chatbot_icon)
        return self

    def click_have_questions(self):
        self.click(self.btn_have_questions)
        return self

    def click_menu_pricing(self):
        self.click(self.btn_menu_pricing)
        return self

    def click_compare_plans(self):
        self.click(self.btn_compare_plans)
        return self

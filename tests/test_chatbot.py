import allure
from pages.chatbot_chat_frame import ChatbotChatFrame
from pages.home_page import HomePage
from pages.pricing_page import PricingPage

@allure.feature("Chatbot chat")
class TestChatbot:

    @allure.story("To pricing page from chat menu.")
    def test_to_pricing_page_from_chat_menu(self, setup):
        # Init pages
        home_page = HomePage(setup)
        chatbot_chat_frame = ChatbotChatFrame(setup)
        pricing_page = PricingPage(setup)
        # Test steps
        home_page.switch_to_frame("chatbot-chat-frame")
        chatbot_chat_frame.click_chatbot_icon() \
            .click_have_questions() \
            .click_menu_pricing() \
            .click_compare_plans()
        assert pricing_page.is_pricing_page()
        assert pricing_page.has_pricing_title()
        pricing_page.screenshot_as_png("To pricing page from chat menu.")

    @allure.story("To pricing page from chat message.")
    def test_to_pricing_page_from_chat_message(self ,setup):
        home_page = HomePage(setup)
        chatbot_chat_frame = ChatbotChatFrame(setup)
        pricing_page = PricingPage(setup)
        home_page.switch_to_frame("chatbot-chat-frame")
        chatbot_chat_frame.click_chatbot_icon()
        assert chatbot_chat_frame.has_greet_message()
        chatbot_chat_frame.send_message("I want to know the price") \
            .click_compare_plans()
        assert pricing_page.is_pricing_page()
        assert pricing_page.has_pricing_title()
        pricing_page.screenshot_as_png("To pricing page from chat message.")
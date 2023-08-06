import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def input(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
        return self

    def click(self, locator):
        self.driver.find_element(*locator).click()
        return self

    def switch_to_frame(self, frame_id):
        self.driver.switch_to.frame(frame_id)
        return self

    def wait_url_changed(self, url):
        try :
            WebDriverWait(self.driver, 10).until(EC.url_contains(url))
            return True
        except:
            return False

    def has_element(self, by_locator, wait_seconds) -> bool:
        self.driver.implicitly_wait(wait_seconds)
        elements = self.driver.find_elements(*by_locator)
        self.driver.implicitly_wait(10)
        return len(elements) > 0

    def screenshot_as_png(self, title):
        if hasattr(self.driver, "get_screenshot_as_png"):
            allure.attach(self.driver.get_screenshot_as_png(), title, allure.attachment_type.PNG)
        return self


from time import sleep
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    global driver
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.get("https://www.chatbot.com/chatbot-demo/")
    yield driver
    sleep(2)
    driver.quit()
    driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if hasattr(driver, "get_screenshot_as_png"):
            allure.attach(driver.get_screenshot_as_png(), "異常截圖", allure.attachment_type.PNG)


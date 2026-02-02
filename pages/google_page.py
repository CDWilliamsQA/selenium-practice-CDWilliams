from utils.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)


class GooglePage: # name doesn't matter
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    TEXT_INPUT = (By.NAME, "my-text")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        logger.info("Opening Selenium test form page")
        self.driver.get(self.URL)

    def handle_consent(self):
        # No consent on this page — keep method for framework consistency
        pass

    def search(self, text):
        logger.info(f"Entering text: {text}")
        input_box = self.wait.until(EC.visibility_of_element_located(self.TEXT_INPUT))
        input_box.clear()
        input_box.send_keys(text)

        logger.info("Submitting form")
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
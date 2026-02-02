from utils.logger import get_logger
logger = get_logger(__name__)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    SEARCH_BOX = (By.NAME, "q")
    ACCEPT_BUTTON = (By.XPATH, "//button/div[contains(text(),'Accept all')]")

    def open(self):
        logger.info("Opening Google homepage")
        self.driver.get("https://www.google.com")

    def handle_consent(self):
        try:
            logger.info("Checking for consent pop-up")
            accept_btn = self.wait.until(
                EC.element_to_be_clickable(self.ACCEPT_BUTTON)
            )
            accept_btn.click()
            logger.info("Consent pop-up handled")
        except Exception:
            logger.info("No consent pop-up present")

    def search(self, text):
        logger.info(f"Searching Google for: {text}")
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.send_keys(text)
        search_box.submit()
        logger.info("Search submitted")


from utils.logger import get_logger
logger = get_logger(__name__)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    RESULTS = (By.CSS_SELECTOR, "div.g")

    def get_results(self):
        logger.info("Waiting for search results to be visible")
        results = self.wait.until(
            EC.visibility_of_all_elements_located(self.RESULTS)
        )
        logger.info(f"{len(results)} results found on page")
        return results

    def results_exist(self):
        logger.info("Checking if any search results exist")
        return len(self.get_results()) > 0

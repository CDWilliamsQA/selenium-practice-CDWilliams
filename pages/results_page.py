from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultsPage:
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def results_exist(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.MESSAGE))
            return True
        except:
            return False
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()

    # Run headless ONLY when HEADLESS=true
    if os.getenv("HEADLESS", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Only maximize when not headless (optional, but avoids weirdness)
    if os.getenv("HEADLESS", "").lower() != "true":
        driver.maximize_window()

    return driver
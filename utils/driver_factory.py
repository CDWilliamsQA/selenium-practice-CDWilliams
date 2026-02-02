import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()

    # ===============================
    # HEADLESS MODE (used in CI)
    # ===============================
    # Only run headless if HEADLESS=true
    if os.getenv("HEADLESS", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # ===============================
    # Create driver
    # ===============================
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # ===============================
    # Maximize window when NOT headless
    # ===============================
    if os.getenv("HEADLESS", "").lower() != "true":
        driver.maximize_window()

    return driver

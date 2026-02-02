from pages.google_page import GooglePage
from pages.results_page import ResultsPage


# ✅ PASS TEST
def test_google_title(driver):
    google = GooglePage(driver)
    google.open()
    assert "Google" in driver.title


# ❌ FAIL TEST (forces screenshot via conftest hook)
def test_google_search_failure(driver):
    google = GooglePage(driver)
    google.open()
    google.handle_consent()
    google.search("Selenium Python tutorial")

    results = ResultsPage(driver)
    assert results.results_exist() # this should PASS

    # Intentionally wrong assertion to force FAIL + screenshot
    assert "THIS_TEXT_DOES_NOT_EXIST" in driver.page_source

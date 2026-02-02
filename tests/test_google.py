import pytest
from pages.google_page import GooglePage
from pages.results_page import ResultsPage


def test_form_submission(driver):
    page = GooglePage(driver)
    page.open()
    page.handle_consent()
    page.search("Automation Test")

    results = ResultsPage(driver)
    assert results.results_exist(), "Form submission did not succeed"


def test_url_changed_after_submit(driver):
    page = GooglePage(driver)
    page.open()
    page.search("Hello")

    assert "submitted" in driver.current_url or "message" in driver.page_source


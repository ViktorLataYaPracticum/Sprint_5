import pytest
from selenium import webdriver
from locators import PageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(PageLocators.SERVICE_URL)
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.SERVICE_URL)
    yield driver
    driver.quit()

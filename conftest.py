import pytest
from selenium import webdriver
from locators import PageLocators
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    #service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(PageLocators.SERVICE_URL)
    yield driver
    driver.quit()

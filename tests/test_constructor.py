import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from selenium.webdriver.common.by import By


#Проверка перехода к разделу "Булки"
def test_constructor_tabs_buns(driver):
    driver.find_element(By.XPATH, PageLocators.SAUCES_TAB).click()
    driver.find_element(By.XPATH, PageLocators.BUNS_TAB).click()
    assert driver.find_element(By.XPATH,PageLocators.BUNS_H2).is_displayed()

#Проверка перехода к разделу "Соусы"
def test_constructor_tabs_sauces(driver):
    driver.find_element(By.XPATH, PageLocators.SAUCES_TAB).click()
    assert driver.find_element(By.XPATH,PageLocators.SAUCES_H2).is_displayed()

#Проверка перехода к разделу "Начинки"
def test_constructor_tabs_fillings(driver):
    driver.find_element(By.XPATH, PageLocators.FILLINGS_TAB).click()
    assert driver.find_element(By.XPATH,PageLocators.FILLINGS_H2).is_displayed()

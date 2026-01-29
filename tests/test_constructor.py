import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from selenium.webdriver.common.by import By
from constants import Constants


#Проверка перехода к разделу "Булки"
def test_constructor_tabs_buns(driver):
    driver.find_element(By.XPATH, ConstructorPageLocators.SAUCES_TAB).click()
    tab=driver.find_element(By.XPATH, ConstructorPageLocators.BUNS_TAB)
    tab.click()
    assert driver.find_element(By.XPATH,ConstructorPageLocators.BUNS_H2).is_displayed()
    assert  Constants.ACTIVE_TAB_CLASS in tab.find_element(By.XPATH,"parent::div").get_attribute("class").split()

#Проверка перехода к разделу "Соусы"
def test_constructor_tabs_sauces(driver):
    tab=driver.find_element(By.XPATH, ConstructorPageLocators.SAUCES_TAB)
    tab.click()
    assert driver.find_element(By.XPATH,ConstructorPageLocators.SAUCES_H2).is_displayed()
    assert  Constants.ACTIVE_TAB_CLASS in tab.find_element(By.XPATH,"parent::div").get_attribute("class").split()

#Проверка перехода к разделу "Начинки"
def test_constructor_tabs_fillings(driver):
    tab=driver.find_element(By.XPATH, ConstructorPageLocators.FILLINGS_TAB)
    tab.click()
    assert driver.find_element(By.XPATH,ConstructorPageLocators.FILLINGS_H2).is_displayed()
    assert  Constants.ACTIVE_TAB_CLASS in tab.find_element(By.XPATH,"parent::div").get_attribute("class").split()

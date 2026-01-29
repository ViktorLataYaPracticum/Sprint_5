import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from constants import Constants
from selenium.webdriver.common.by import By


# Переход в личный кабинет по клику на ссылку «Личный кабинет».
def test_go_to_personal_account(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    driver.find_element(By.XPATH,MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, AccountPageLocators.LOGOUT_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL+"account/profile"

#выход по кнопке «Выйти» в личном кабинете
def test_logout(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    driver.find_element(By.XPATH,MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, AccountPageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.XPATH,AccountPageLocators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL+"login"


#Переход из личного кабинета в конструктор по нажатию на ссылку "Конструктор"
def test_go_to_constructor_from_account_by_link_constructor(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    driver.find_element(By.XPATH,MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, AccountPageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.XPATH,MainPageLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL

#Переход из личного кабинета в конструктор при нажатии на логотип 
def test_go_to_constructor_from_account_by_logo(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    driver.find_element(By.XPATH,MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, AccountPageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.CSS_SELECTOR,MainPageLocators.LOGO).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL
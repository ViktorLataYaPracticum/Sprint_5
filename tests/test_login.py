import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from constants import Constants

#Успешная авторизация через кнопку на главной странице
def test_login_from_main_page(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL

#Успешная авторизация через ссылку "Личный кабинет"
def test_login_from_personal_account(driver):
    driver.find_element(By.XPATH,MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, LoginPageLocators.LOGIN_BUTTON))
    )
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL

#Успешная авторизация через ссылку на странице регистрации
def test_login_from_registration_form(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, LoginPageLocators.REGISTER_LINK))
    )
    driver.find_element(By.LINK_TEXT, LoginPageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, RegisterPageLocators.LOGIN_LINK))
    )
    driver.find_element(By.LINK_TEXT,RegisterPageLocators.LOGIN_LINK).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, LoginPageLocators.LOGIN_BUTTON))
    )
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )

    assert driver.current_url == Constants.SERVICE_URL

#Успешная авторизация через ссылку на странице восстановления пароля
def test_login_from_password_recovery(driver):
    driver.find_element(By.XPATH,MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, LoginPageLocators.FORGOT_PASSWORD_LINK))
    )
    driver.find_element(By.LINK_TEXT, LoginPageLocators.FORGOT_PASSWORD_LINK).click()
    
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, RegisterPageLocators.LOGIN_LINK))
    )
    driver.find_element(By.LINK_TEXT, RegisterPageLocators.LOGIN_LINK).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, LoginPageLocators.LOGIN_BUTTON))
    )
    driver.find_element(By.NAME,LoginPageLocators.EMAIL_INPUT).send_keys(Constants.TEST_LOGIN)
    driver.find_element(By.NAME, LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, MainPageLocators.GETORDER_BUTTON))
    )
    assert driver.current_url == Constants.SERVICE_URL

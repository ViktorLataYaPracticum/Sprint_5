import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import PageLocators

#Успешная авторизация через кнопку на главной странице
def test_login_from_main_page(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    current_url=driver.current_url
    driver.quit()
    assert current_url == PageLocators.SERVICE_URL

#Успешная авторизация через ссылку "Личный кабинет"
def test_login_from_personal_account(driver):
    driver.find_element(By.XPATH,PageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
    )
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    current_url=driver.current_url
    driver.quit()
    assert current_url == PageLocators.SERVICE_URL

#Успешная авторизация через ссылку на странице регистрации
def test_login_from_registration_form(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, PageLocators.REGISTER_LINK))
    )
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, PageLocators.LOGIN_LINK_REGISTER))
    )
    driver.find_element(By.LINK_TEXT,PageLocators.LOGIN_LINK_REGISTER).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
    )
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    current_url=driver.current_url
    driver.quit()
    assert current_url == PageLocators.SERVICE_URL

#Успешная авторизация через ссылку на странице восстановления пароля
def test_login_from_password_recovery(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, PageLocators.FORGOT_PASSWORD_LINK))
    )
    driver.find_element(By.LINK_TEXT, PageLocators.FORGOT_PASSWORD_LINK).click()
    
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, PageLocators.LOGIN_LINK_REGISTER))
    )
    driver.find_element(By.LINK_TEXT, PageLocators.LOGIN_LINK_REGISTER).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
    )
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    current_url=driver.current_url
    driver.quit()
    assert current_url == PageLocators.SERVICE_URL

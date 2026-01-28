import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from selenium.webdriver.common.by import By


# Переход в личный кабинет по клику на ссылку «Личный кабинет».
def test_go_to_personal_account(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    driver.find_element(By.XPATH,PageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.LOGOUT_BUTTON))
    )
    assert driver.current_url == PageLocators.SERVICE_URL+"account/profile"

#выход по кнопке «Выйти» в личном кабинете
def test_logout(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    driver.find_element(By.XPATH,PageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.XPATH,PageLocators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
    )
    assert driver.current_url == PageLocators.SERVICE_URL+"login"


#Переход из личного кабинета в конструктор по нажатию на ссылку "Конструктор"
def test_go_to_constructor_from_account_by_link_constructor(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    driver.find_element(By.XPATH,PageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.XPATH,PageLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    assert driver.current_url == PageLocators.SERVICE_URL

#Переход из личного кабинета в конструктор при нажатии на логотип 
def test_go_to_constructor_from_account_by_logo(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.NAME,PageLocators.EMAIL_INPUT_LOGIN).send_keys(PageLocators.TEST_LOGIN)
    driver.find_element(By.NAME, PageLocators.PASSWORD_INPUT_LOGIN).send_keys(PageLocators.TEST_PASSWORD)
    driver.find_element(By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    driver.find_element(By.XPATH,PageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, PageLocators.LOGOUT_BUTTON))
    )
    driver.find_element(By.CSS_SELECTOR,PageLocators.LOGO).click()

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, PageLocators.GETORDER_BUTTON_MAIN))
    )
    assert driver.current_url == PageLocators.SERVICE_URL
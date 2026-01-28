import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import PageLocators
from selenium.webdriver.common.by import By
from generator import generate_email


#Успешная регистрация при не пустом поле имени, email в формате логин@домен, пароля не меньше 6 символов
@pytest.mark.parametrize('password', ['123456', '1234567'])
def test_successful_registration(driver,password):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    driver.find_element(By.XPATH, PageLocators.NAME_INPUT).send_keys("Viktor")
    driver.find_element(By.XPATH, PageLocators.EMAIL_INPUT_REGISTER).send_keys(generate_email())
    driver.find_element(By.XPATH, PageLocators.PASSWORD_INPUT_REGISTER).send_keys(password)
    driver.find_element(By.XPATH, PageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN)))
    driver.quit()

#Отказ системы в регистрации при пустом поле имени, email в формате логин@домен, пароля не меньше 6 символов
def test_unsuccessful_registration_empty_name(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    driver.find_element(By.XPATH, PageLocators.NAME_INPUT).clear()
    driver.find_element(By.XPATH, PageLocators.EMAIL_INPUT_REGISTER).send_keys(generate_email())
    driver.find_element(By.XPATH, PageLocators.PASSWORD_INPUT_REGISTER).send_keys("123456")
    driver.find_element(By.XPATH, PageLocators.REGISTER_BUTTON).click()

    # Проверяем, что элемент успешной авторизации НЕ появился
    with pytest.raises(TimeoutException):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
        )
    driver.quit()    

#Отказ системы в регистрации при не пустом поле имени, не корректном email (не в формате логин@домен или пустое поле), корректном пароле не меньше 6 символов

@pytest.mark.parametrize('params', ['test.test', 
                                  ''])
def test_unsuccessful_registration_incorrect_email(driver,params):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    driver.find_element(By.XPATH, PageLocators.NAME_INPUT).send_keys("Viktor")
    driver.find_element(By.XPATH, PageLocators.EMAIL_INPUT_REGISTER).send_keys(params)
    driver.find_element(By.XPATH, PageLocators.PASSWORD_INPUT_REGISTER).send_keys("123456")
    driver.find_element(By.XPATH, PageLocators.REGISTER_BUTTON).click()

    # Проверяем, что элемент успешной авторизации НЕ появился
    with pytest.raises(TimeoutException):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
        )
    driver.quit()    

#Отказ системы в регистрации при пустом поле имени, пустом email, корректном пароле не меньше 6 символов
def test_unsuccessful_registration_empty_email_empty_name(driver):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    driver.find_element(By.XPATH, PageLocators.NAME_INPUT).clear()
    driver.find_element(By.XPATH, PageLocators.EMAIL_INPUT_REGISTER).clear()
    driver.find_element(By.XPATH, PageLocators.PASSWORD_INPUT_REGISTER).send_keys("123456")
    driver.find_element(By.XPATH, PageLocators.REGISTER_BUTTON).click()

    # Проверяем, что элемент успешной авторизации НЕ появился
    with pytest.raises(TimeoutException):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, PageLocators.LOGIN_BUTTON_LOGIN))
        )
    driver.quit()

#Отказ системы в регистрации при НЕкорректном пароле меньше 6 символов/пустое поле
@pytest.mark.parametrize('password', ['', 
                                  '1', 
                                  '12',
                                  '12345'])
def test_unsaccessful_registration_with_incorrect_password_show_error(driver,password):
    driver.find_element(By.XPATH,PageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(By.LINK_TEXT, PageLocators.REGISTER_LINK).click()

    driver.find_element(By.XPATH, PageLocators.NAME_INPUT).send_keys("Viktor")
    driver.find_element(By.XPATH, PageLocators.EMAIL_INPUT_REGISTER).send_keys(generate_email())
    driver.find_element(By.XPATH, PageLocators.PASSWORD_INPUT_REGISTER).send_keys(password)
    driver.find_element(By.XPATH, PageLocators.REGISTER_BUTTON).click()

    assert driver.find_element(By.XPATH,PageLocators.PASSWORD_ERROR).is_displayed()

class MainPageLocators:
    #-----------------------------main page-----------------
    LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"                           # Кнопка «Войти в аккаунт»
    PERSONAL_ACCOUNT = "//p[text()='Личный Кабинет']"                                  # Кнопка «Личный кабинет»
    CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']"                                   # Кнопка «Конструктор»
    LOGO = ".AppHeader_header__logo__2D0X2 > a"                                        # Логотип Stellar Burgers
    GETORDER_BUTTON = "//button[text()='Оформить заказ']"                         # Кнопка «Оформить заказ»

class LoginPageLocators: 
#-----------------------------login page---------------- 
    EMAIL_INPUT = "name"                                                         # Поле Email
    PASSWORD_INPUT = "Пароль"                                                    # Поле Пароль
    LOGIN_BUTTON = "//button[text()='Войти']"                                    # Кнопка «Войти»
    REGISTER_LINK = "Зарегистрироваться"                                               # Ссылка «Зарегистрироваться»
    FORGOT_PASSWORD_LINK =  "Восстановить пароль"                                      # Ссылка «Восстановить пароль»

class RegisterPageLocators: 
#-----------------------------register page---------------- 
    NAME_INPUT = "//label[text()='Имя']/following-sibling::input"                      # Поле «Имя»
    EMAIL_INPUT = "//label[text()='Email']/following-sibling::input"          # Поле Email
    PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"      # Поле Пароль
    REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"                          # Кнопка регистрации
    PASSWORD_ERROR = "//p[text()='Некорректный пароль']"                               # Ошибка пароля
    LOGIN_LINK = "Войти"                                                      #Ссылка "Войти"

class AccountPageLocators: 
#-----------------------------account page---------------- 
    LOGOUT_BUTTON = "//button[text()='Выход']"                                         # Кнопка «Выйти»

class ConstructorPageLocators: 
#-----------------------------constructor---------------- 
    BUNS_TAB =  "//span[text()='Булки']"                                               # Таб «Булки»
    SAUCES_TAB =  "//span[text()='Соусы']"                                             # Таб «Соусы»
    FILLINGS_TAB = "//span[text()='Начинки']"                                          # Таб «Начинки»
    BUNS_H2 =  "//main/section/div/h2[text()='Булки']"                                 # Заголовок «Булки»
    SAUCES_H2 =  "//main/section/div/h2[text()='Соусы']"                               # Заголовок «Соусы»
    FILLINGS_H2 = "//main/section/div/h2[text()='Начинки']"                            # Заголовок «Начинки»

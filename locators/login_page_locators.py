import allure
from selenium.webdriver.common.by import By


class LoginPageLocators:

    FORGOT_PASSWORD = (By.XPATH, "//a[@href = '/forgot-password']")
    EMAIL_INPUT_IN_LOGIN = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']")  # поле для ввода почты
    PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input[@type = 'password']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']/parent::a")  # кнопка Конструктор

    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon')]")
    EYE_BUTTON_STYLE = (By.XPATH, "//div[contains(@class,'input__icon')]/preceding::input[@name= 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//h2[text() = 'Вход']")  # Надпись Вход
    BUTTON_GO = (By.XPATH, "//button[text() = 'Войти']")  # кнопка Войти
    LIST_ORDER = (By.XPATH, "//ul[contains(@class,'OrderHistory_profileList')]")  # список заказов

import allure
from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_BUTTON = (By.XPATH, "//a[@href = '/account']") # ссылка на Личный Кабинет

    REGISTRATION_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']") #ссылка для регистрации

    LOGIN_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@type = 'text']") #поле для ввода имени
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']") #поле для ввода почты
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") #поле для ввода пароля
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # кнопка регистрации
    BUTTON_GO= (By.XPATH, "//button[text() = 'Войти']") #кнопка Войти
    REG_FALSE = (By.XPATH, "//p[text() = 'Такой пользователь уже существует']") #поле Такой пользователь уже существует
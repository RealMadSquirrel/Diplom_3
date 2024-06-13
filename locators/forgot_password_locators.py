import allure
from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']")  # поле для ввода почты
    RESTORE_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")  # Восстановить
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']/parent::a")  # кнопка Конструктор

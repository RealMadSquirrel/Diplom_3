import allure
from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    EMAIL_INPUT_IN_FORGOT_PAGE = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']")  # поле для ввода почты
    RESTORE_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")  # Восстановить

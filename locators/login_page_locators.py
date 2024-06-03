import allure
from selenium.webdriver.common.by import By

class LoginPageLocators:
    PERSONAL_BUTTON = (By.XPATH, "//a[@href = '/account']") # ссылка на Личный Кабинет
    FORGOT_PASSWORD = (By.XPATH, "//a[@href = '/forgot-password']")
    EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']")  # поле для ввода почты
    RESTORE_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']") # Восстановить
    RESTORE_BUTTON = (By.XPATH, "//h2[text() = 'Восстановление пароля']")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon')]")
    EYE_BUTTON_STYLE = (By.XPATH, "//div[contains(@class,'input__icon')]/preceding::input[@name= 'Пароль']")
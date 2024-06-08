import allure
from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_BUTTON = (By.XPATH, "//a[@href = '/account']") # ссылка на Личный Кабинет
    PROFILE_TITLE = (By.XPATH, "//a[@href = '/account/profile']")
    LENTA_ORDERS = (By.XPATH, "//h1[text() = 'Лента заказов']")
    LENTA_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']/parent::a")
    LOGIN_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@type = 'text']") #поле для ввода имени
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']") #поле для ввода почты
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") #поле для ввода пароля
    BUTTON_GO= (By.XPATH, "//button[text() = 'Войти']") #кнопка Войти
    ORDER_IDENTIFICATOR = (By.XPATH, "//li[contains(@class,'OrderHistory')]/a/div/p[1]")
    CROSS_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")  # ссылка на Личный Кабинет
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")



from selenium.webdriver.common.by import By


class AccountPageLocators:
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")  # ссылка на Личный Кабинет
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    ORDER_IDENTIFICATOR = (By.XPATH, "//li[contains(@class,'OrderHistory')]/a/div/p[1]")

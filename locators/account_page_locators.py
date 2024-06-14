from selenium.webdriver.common.by import By


class AccountPageLocators:

    PROFILE_TITLE = (By.XPATH, "//a[@href = '/account/profile']")
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    ORDER_IDENTIFICATOR_IN_HISTORY = (By.XPATH, "//li[contains(@class,'OrderHistory')]/a/div/p[1]")

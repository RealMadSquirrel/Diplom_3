import allure
from selenium.webdriver.common.by import By


class OrdersLentaPageLocators:

    ORDER_IDENTIFICATOR = (By.XPATH, "//li[contains(@class,'OrderHistory')]/a/div/p[1]")
    ANY_ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory')]/following::p[1]")  # для клика на любой заказ
    MODAL_WINDOW_ORDERS = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    LENTA_ORDERS = (By.XPATH, "//h1[text() = 'Лента заказов']")
    LENTA_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']/parent::a")
    COMPLETED_ALL_TIME = (By.XPATH, "//p[text() = 'Выполнено за все время:']/following::p[1]")
    COMPLETED_TODAY = (By.XPATH, "//p[text() = 'Выполнено за все время:']/following::p[3]")

    IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

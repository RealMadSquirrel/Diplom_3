import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.orders_lenta_locators import OrdersLentaPageLocators
from pages.base_page import BasePage


class OrderLentaPage(BasePage):

    @allure.step('Кликаем на кнопку ингредиент')
    def click_to_ingredient(self):
        self.wait_clickable_find_element_click(OrdersLentaPageLocators.ANY_ORDER)

    @allure.step('Проверяем, что окно с деталями на странице ленты заказов присутствует')
    def check_exists_modal_window_orders(self):
        return self.check_exists_by_xpath(OrdersLentaPageLocators.MODAL_WINDOW_ORDERS)

    @allure.step('Поиск идентификатора заказа в ленте заказов')
    def search_order_id_in_lenta(self):
        return self.wait_and_find_element(OrdersLentaPageLocators.ORDER_IDENTIFICATOR_IN_LENTA).text

    @allure.step('Поиск числа заказов, выполненных за все время')
    def search_all_completed_order_in_lenta(self):
        return self.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_ALL_TIME).text

    @allure.step('Поиск числа заказов, выполненных за сегодня')
    def search_today_completed_order_in_lenta(self):
        return self.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_TODAY).text


    @allure.step('Поиск номера заказа в разделе В работе')
    def search_number_orders_in_work(self):
        return self.get_order_number_in_work(OrdersLentaPageLocators.IN_WORK)

    @allure.step('Поиск заголовка Лента заказов')
    def search_lenta_orders(self):
        return self.wait_and_find_element(OrdersLentaPageLocators.LENTA_ORDERS).text

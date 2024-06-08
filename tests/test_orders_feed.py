import allure
import json
import time
from pages.login_page import LoginPage
from pages.orders_lenta_page import OrderLentaPage
from locators.orders_lenta_locators import OrdersLentaPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.main_functionality_locators import MainFuncPageLocators
from data import Urls
from data import Data
from helper import UserApi


class TestOrdersLentaPage:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver):
        order_lenta_page = OrderLentaPage(driver)
        order_lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        order_lenta_page.wait_clickable_find_element_click(OrdersLentaPageLocators.ANY_ORDER)
        assert order_lenta_page.check_exists_by_xpath(OrdersLentaPageLocators.MODAL_WINDOW_ORDERS)

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_lenta_and_history(self, driver, create_creds_user):
        page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        page.open_page(Urls.BASE_URL + Urls.LOGIN)
        page.set_email_input(create_creds_user['email'])
        page.set_password_input(create_creds_user['password'])
        page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        page.wait_and_find_element(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN)
        page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)
        page.open_page(Urls.BASE_URL + Urls.ACCOUNT)
        page.wait_and_click_to_element(MainPageLocators.HISTORY_ORDER_BUTTON)
        order_id_in_history = page.wait_and_find_element(MainPageLocators.ORDER_IDENTIFICATOR).text
        page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert order_id_in_history == page.wait_and_find_element(MainPageLocators.ORDER_IDENTIFICATOR).text

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_count_all_time_increases(self, driver, create_creds_user):
        page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        page.open_page(Urls.BASE_URL + Urls.LOGIN)
        page.set_email_input(create_creds_user['email'])
        page.set_password_input(create_creds_user['password'])
        page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        page.wait_and_click_to_element(MainFuncPageLocators.LENTA_BUTTON)
        completed_all_time_1 = page.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_ALL_TIME).text
        page.click_to_element_with_js(MainFuncPageLocators.CONSTRUCTOR_BUTTON)
        page.wait_and_find_element(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN)
        page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.LENTA_BUTTON)
        UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert int(completed_all_time_1) < int(
            page.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_ALL_TIME).text)

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_count_today_increases(self, driver, create_creds_user):
        page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        page.open_page(Urls.BASE_URL + Urls.LOGIN)
        page.set_email_input(create_creds_user['email'])
        page.set_password_input(create_creds_user['password'])
        page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        page.wait_and_click_to_element(MainFuncPageLocators.LENTA_BUTTON)
        completed_today_1 = page.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_TODAY).text
        page.click_to_element_with_js(MainFuncPageLocators.CONSTRUCTOR_BUTTON)
        page.wait_and_find_element(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN)
        page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.LENTA_BUTTON)
        UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert int(completed_today_1) < int(page.wait_and_find_element(OrdersLentaPageLocators.COMPLETED_TODAY).text)

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    def test_order_in_work(self, driver, create_creds_user):
        page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        page.open_page(Urls.BASE_URL + Urls.LOGIN)
        page.set_email_input(create_creds_user['email'])
        page.set_password_input(create_creds_user['password'])
        page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        page.wait_and_find_element(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN)
        page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_BUTTON)
        page.click_to_element_with_js(MainFuncPageLocators.CHECKOUT_BUTTON)
        number_order = page.get_new_order_number(OrdersLentaPageLocators.NUMBER_ORDERS)
        page.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)
        page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert number_order in page.get_order_number_in_work(OrdersLentaPageLocators.IN_WORK)







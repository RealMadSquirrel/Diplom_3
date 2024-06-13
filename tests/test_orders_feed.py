import allure
import json
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_lenta_page import OrderLentaPage
from pages.account_page import AccountPage
from locators.account_page_locators import AccountPageLocators
from locators.orders_lenta_locators import OrdersLentaPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators

from data import Urls
from data import Data
from helper import UserApi


class TestOrdersLentaPage:

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order(self, driver):
        order_lenta_page = OrderLentaPage(driver)
        order_lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        order_lenta_page.click_to_ingredient()
        assert order_lenta_page.check_exists_modal_window_orders()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_lenta_and_history(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()

        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.add_ingredient_to_order_and_checkout()
        main_page.click_to_cross()

        account_page = AccountPage(driver)
        account_page.open_page(Urls.BASE_URL + Urls.ACCOUNT)
        account_page.wait_url_to_be(Urls.BASE_URL + Urls.PERSONAL_ACCOUNT)
        account_page.click_button_history()
        account_page.wait_url_to_be(Urls.BASE_URL + Urls.HISTORY_URL)

        order_id_in_history = account_page.search_order_id_in_history()

        lenta_page = OrderLentaPage(driver)
        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        assert order_id_in_history == lenta_page.search_order_id_in_lenta()

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_order_count_all_time_increases(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()

        lenta_page = OrderLentaPage(driver)
        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        completed_all_time_1 = lenta_page.search_all_completed_order_in_lenta()

        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.add_ingredient_to_order_and_checkout()
        main_page.click_to_cross()

        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        lenta_page.wait_url_to_be(Urls.BASE_URL + Urls.LENTA_ORDERS)
        assert int(completed_all_time_1) < int(lenta_page.search_all_completed_order_in_lenta())

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_order_count_today_increases(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()

        lenta_page = OrderLentaPage(driver)
        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        completed_today_1 = lenta_page.search_today_completed_order_in_lenta()

        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.add_ingredient_to_order_and_checkout()
        main_page.click_to_cross()

        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        assert int(completed_today_1) < int(lenta_page.search_today_completed_order_in_lenta())

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    def test_order_in_work(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()

        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.add_ingredient_to_order_and_checkout()
        number_order = main_page.search_number_orders_in_modal_window()
        main_page.click_to_cross()

        lenta_page = OrderLentaPage(driver)
        lenta_page.open_page(Urls.BASE_URL + Urls.LENTA_ORDERS)
        assert number_order in lenta_page.search_number_orders_in_work()







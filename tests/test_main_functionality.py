import allure
import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.orders_lenta_page import OrderLentaPage
from locators.login_page_locators import LoginPageLocators
from locators.orders_lenta_locators import OrdersLentaPageLocators
from locators.main_page_locators import MainPageLocators
from data import Urls
from data import Data
import selectors
from seletools.actions import drag_and_drop
from helper import UserApi


class TestMainFuncPage:

    @allure.title("Клик по кнопке Конструктор")
    def test_click_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.click_constructor()
        login_page.wait_for_url_changes_login()
        main_page = MainPage(driver)
        assert main_page.search_title_collect_burger() == 'Соберите бургер'

    @allure.title("Клик по кнопке Лента")
    def test_click_lenta(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_order_lenta()
        lenta_page = OrderLentaPage(driver)
        assert lenta_page.search_lenta_orders() == 'Лента заказов'

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_to_ingredient()
        assert main_page.search_title_details_ingredient() == 'Детали ингредиента'

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_cross_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_to_ingredient_and_closed()
        assert main_page.info_ingredient_is_invisible()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_count_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        count_one = main_page.count_ingredient()
        main_page.add_ingredient_to_order_main_page()
        count_two = main_page.count_ingredient()
        assert count_one != count_two

    @allure.title("Залогированный пользователь может оформить заказ.")
    def test_checkout(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()

        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.add_ingredient_to_order_and_checkout()

        assert main_page.search_checkout_text() == 'Ваш заказ начали готовить'

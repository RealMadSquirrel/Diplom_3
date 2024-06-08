import allure
import time
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.main_functionality_locators import MainFuncPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.orders_lenta_locators import OrdersLentaPageLocators
from data import Urls
from data import Data
import selectors
from seletools.actions import drag_and_drop
from helper import UserApi


class TestMainFuncPage:

    @allure.title("Клик по кнопке Конструктор")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_to_element_with_js(MainFuncPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.wait_and_find_element(MainFuncPageLocators.BUILD_BURGER).text == 'Соберите бургер'

    @allure.title("Клик по кнопке Лента")
    def test_click_lenta(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        lenta_order = main_page.click_order_lenta()
        assert lenta_order.wait_and_find_element(OrdersLentaPageLocators.LENTA_ORDERS).text == 'Лента заказов'

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_to_element_with_js(MainFuncPageLocators.INGREDIENT_BUTTON)
        assert main_page.wait_and_find_element(MainFuncPageLocators.H2_DETAILS_INGR).text == 'Детали ингредиента'

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_croos_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        main_page.click_to_element_with_js(MainFuncPageLocators.INGREDIENT_BUTTON)
        main_page.click_to_element_with_js(MainFuncPageLocators.CROSS_BUTTON)

        assert main_page.element_is_invisible(MainFuncPageLocators.CROSS_BUTTON)

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_count_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.BASE_URL)
        count_one = main_page.wait_and_find_element(MainFuncPageLocators.COUNT_INGREDIENTS).text
        main_page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        count_two = main_page.wait_and_find_element(MainFuncPageLocators.COUNT_INGREDIENTS).text
        assert count_one != count_two

    @allure.title("Залогированный пользователь может оформить заказ.")
    def test_checkout(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        main_page = login_page.click_button_go()
        main_page.wait_and_find_element(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN)
        main_page.add_ingredient_to_order(MainFuncPageLocators.INGREDIENT_BUTTON_KRATEN, MainFuncPageLocators.TARGET)
        main_page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_BUTTON)
        main_page.click_to_element_with_js(MainFuncPageLocators.CHECKOUT_BUTTON)
        UserApi.delete_user(created_user_request.json()[
                                "accessToken"])
        assert main_page.wait_and_find_element(MainFuncPageLocators.CHECKOUT_TEXT).text == 'Ваш заказ начали готовить'

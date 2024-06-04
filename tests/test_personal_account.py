import allure
import time
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators
from data import Urls
from data import Data


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Переходим на страницу /login и кликаем по ЛК")
    def test_go_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.wait_and_click_to_element(LoginPageLocators.PERSONAL_BUTTON)
        assert login_page.wait_and_find_element(LoginPageLocators.LOGIN_BUTTON).text == 'Вход'

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_history_order(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(Data.EMAIL)
        login_page.set_password_input(Data.PASSWORD)
        login_page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        login_page.wait_clickable_find_element_click(LoginPageLocators.PERSONAL_BUTTON)
        login_page.wait_and_click_to_element(LoginPageLocators.HISTORY_ORDER_BUTTON)
        assert login_page.check_exists_by_xpath(LoginPageLocators.LIST_ORDER)

    @allure.title("Выход из аккаунта")
    @allure.description("Выход из аккаунта")
    def test_go_to_exit(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(Data.EMAIL)
        login_page.set_password_input(Data.PASSWORD)
        login_page.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        login_page.wait_clickable_find_element_click(LoginPageLocators.PERSONAL_BUTTON)
        login_page.wait_and_click_to_element(LoginPageLocators.EXIT_BUTTON)
        assert login_page.check_exists_by_xpath(LoginPageLocators.BUTTON_GO)
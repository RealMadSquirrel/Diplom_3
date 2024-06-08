import allure
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from helper import UserApi
from data import Urls
from data import Data


class TestOrderFeed:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver, create_creds_user ):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        created_user_request = UserApi.create_user(create_creds_user)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        main_page = login_page.click_button_go()
        main_page.click_personal_account()
        UserApi.delete_user(created_user_request.json()[
                                "accessToken"])
        assert main_page.wait_and_find_element(MainPageLocators.PROFILE_TITLE).text == 'Профиль'

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_history_order(self, driver,create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        created_user_request = UserApi.create_user(create_creds_user)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        main_page = login_page.click_button_go()
        main_page.click_personal_account()
        main_page.wait_and_click_to_element(MainPageLocators.HISTORY_ORDER_BUTTON)
        UserApi.delete_user(created_user_request.json()[
                                                      "accessToken"])
        assert main_page.wait_and_find_element(MainPageLocators.HISTORY_ORDER_BUTTON).get_attribute('aria-current') == 'page'

    @allure.title("Выход из аккаунта")
    @allure.description("Выход из аккаунта")
    def test_go_to_exit(self, driver,create_creds_user):
        login_page = LoginPage(driver)
        created_user_request = UserApi.create_user(create_creds_user)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        main_page = login_page.click_button_go()
        main_page.click_personal_account()
        main_page.wait_and_click_to_element(MainPageLocators.EXIT_BUTTON)
        UserApi.delete_user(created_user_request.json()[
                                "accessToken"])
        assert main_page.check_exists_by_xpath(LoginPageLocators.BUTTON_GO)
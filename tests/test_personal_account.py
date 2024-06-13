import allure
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from helper import UserApi
from data import Urls
from data import Data


class TestAccountPage:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver, create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()
        main_page = MainPage(driver)
        main_page.click_personal_account()
        assert main_page.search_profile_title() == 'Профиль'

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_history_order(self, driver,create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()
        main_page = MainPage(driver)
        main_page.click_personal_account()
        main_page.wait_for_url_changes_main()

        main_page.search_and_click_history_button()

        assert main_page.get_atribute_history_button() == 'page'

    @allure.title("Выход из аккаунта")
    def test_go_to_exit(self, driver,create_creds_user):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.set_email_input(create_creds_user['email'])
        login_page.set_password_input(create_creds_user['password'])
        login_page.click_button_go()
        login_page.wait_for_url_changes_login()
        main_page = MainPage(driver)
        main_page.click_personal_account()
        main_page.wait_url_to_be(Urls.BASE_URL + Urls.PERSONAL_ACCOUNT)
        main_page.search_and_click_exit()

        assert main_page.wait_url_to_be(Urls.BASE_URL + Urls.LOGIN)
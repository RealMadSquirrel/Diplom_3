import allure
import time
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators
from data import Urls
from data import Data


class TestLoginPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Нажимаем на ссылку Личный кабинет, нажимаем на Восстановить пароль и проверяем какой стал url")
    def test_go_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.click_auth_button()
        login_page.wait_and_find_element(LoginPageLocators.FORGOT_PASSWORD)
        login_page.click_to_element_with_js(LoginPageLocators.FORGOT_PASSWORD)
        assert login_page.wait_and_find_element(LoginPageLocators.RESTORE_BUTTON).text == 'Восстановление пароля'

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Ввод почты и клик по кнопке «Восстановить»")
    def test_input_email_and_restore(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.FORGOT_PASSWORD)
        login_page.set_email_input(Data.EMAIL)
        login_page.wait_and_click_to_element(LoginPageLocators.RESTORE_BUTTON)
        assert login_page.url_changes(Urls.BASE_URL + Urls.RESET_PASSWORD)

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_get_password_input_state(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        old_style = login_page.wait_and_find_element(LoginPageLocators.EYE_BUTTON_STYLE).get_attribute('type')
        login_page.click_to_element_with_js(LoginPageLocators.EYE_BUTTON)
        new_style = login_page.wait_and_find_element(LoginPageLocators.EYE_BUTTON_STYLE).get_attribute('type')
        assert old_style != new_style

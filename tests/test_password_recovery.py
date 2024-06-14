import allure
import time
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators
from pages.forgot_password_page import ForgotPasswordPage
from locators.forgot_password_locators import ForgotPasswordPageLocators
from data import Urls
from data import Data


class TestLoginPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Нажимаем на кнопку «Восстановить пароль», выполняется переход на страницу /forgot-password")
    def test_go_to_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        login_page.click_restore_password()
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.wait_url_to_be(Urls.BASE_URL + Urls.FORGOT_PASSWORD)

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Создается страница forgot_password_page, заполняется почта, клик по кнопке «Восстановить»")
    def test_input_email_and_restore(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(Urls.BASE_URL + Urls.FORGOT_PASSWORD)
        forgot_password_page.set_email_input(Data.EMAIL)
        forgot_password_page.click_password_restore()
        assert forgot_password_page.wait_url_to_be(Urls.BASE_URL + Urls.RESET_PASSWORD)

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Проверяю изменение атрибута type у элемента глазик")
    def test_get_password_input_state(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        old_style = login_page.get_eye_button_style()
        login_page.click_eye_button()
        new_style = login_page.get_eye_button_style()
        assert old_style != new_style

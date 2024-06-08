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
        forgot_password_page = login_page.click_restore_password()
        assert forgot_password_page.wait_and_find_element(ForgotPasswordPageLocators.RESTORE_BUTTON).text == 'Восстановить'

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description("Создается страница forgot_password_page, заполняется почта, клик по кнопке «Восстановить»")
    def test_input_email_and_restore(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(Urls.BASE_URL + Urls.FORGOT_PASSWORD)
        forgot_password_page.set_email_input(Data.EMAIL)
        forgot_password_page.click_to_element_with_js(ForgotPasswordPageLocators.RESTORE_BUTTON)
        assert forgot_password_page.url_changes(Urls.BASE_URL + Urls.RESET_PASSWORD)

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Проверяю изменение атрибута type у элемента глазик")
    def test_get_password_input_state(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.BASE_URL + Urls.LOGIN)
        old_style = login_page.wait_and_find_element(LoginPageLocators.EYE_BUTTON_STYLE).get_attribute('type')
        login_page.click_to_element_with_js(LoginPageLocators.EYE_BUTTON)
        new_style = login_page.wait_and_find_element(LoginPageLocators.EYE_BUTTON_STYLE).get_attribute('type')
        assert old_style != new_style

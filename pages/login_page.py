import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from data import Urls
class LoginPage(BasePage):

    @allure.step('Заполняем поле Email')
    def set_email_input(self, email):
        login_input = self.wait_and_find_element(LoginPageLocators.EMAIL_INPUT)
        login_input.send_keys(email)

    @allure.step('Заполняем поле Password')
    def set_password_input(self, password):
        login_input = self.wait_and_find_element(LoginPageLocators.PASSWORD_INPUT)
        login_input.send_keys(password)

    @allure.step('Кликаем на кнопку Войти')
    def click_button_go(self):
        self.wait_and_find_element(LoginPageLocators.BUTTON_GO)
        self.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        return MainPage(self.driver)


    @allure.step('Кликаем по кнопке «Восстановить пароль»')
    def click_restore_password(self):
        self.wait_and_find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.click_to_element_with_js(LoginPageLocators.FORGOT_PASSWORD)

    @allure.step('Кликаем по кнопке «Войти»')
    def click_go_to_button(self):
        self.click_to_element_with_js(LoginPageLocators.BUTTON_GO)


    @allure.step('Ожидание смены страницы логина')
    def wait_for_url_changes_login(self):
        self.wait_url_changes(Urls.BASE_URL + Urls.LOGIN)

    @allure.step('Кликаем на кнопку Конструктор')
    def click_constructor(self):
        self.click_to_element_with_js(LoginPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Берем стиль глазика скрыть/посмотреть пароль')
    def get_eye_button_style(self):
        return self.wait_and_find_element(LoginPageLocators.EYE_BUTTON_STYLE).get_attribute('type')

    @allure.step('Кликаем на глазик скрыть/посмотреть пароль')
    def click_eye_button(self):
        return self.click_to_element_with_js(LoginPageLocators.EYE_BUTTON)



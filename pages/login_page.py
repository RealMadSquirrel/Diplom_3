import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage

class LoginPage(BasePage):

    @allure.step('Заполняем поле Email')
    def set_email_input(self, email):
        login_input = self.wait_and_find_element(LoginPageLocators.EMAIL_INPUT)
        login_input.send_keys(email)

    @allure.step('Заполняем поле Password')
    def set_password_input(self, password):
        login_input = self.wait_and_find_element(LoginPageLocators.PASSWORD_INPUT)
        login_input.send_keys(password)

    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_button_go(self):
        self.wait_and_find_element(LoginPageLocators.BUTTON_GO)
        self.click_to_element_with_js(LoginPageLocators.BUTTON_GO)
        return MainPage(self.driver)


    @allure.step('Кликаем по кнопке «Восстановить пароль»')
    def click_restore_password(self):
        self.wait_and_find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.click_to_element_with_js(LoginPageLocators.FORGOT_PASSWORD)
        return ForgotPasswordPage(self.driver)

import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage



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
    def click_auth_button(self):
        button = self.wait_and_find_element(MainPageLocators.PERSONAL_BUTTON)
        button.click()
        return LoginPage(self.driver)

    @allure.step('Возвращает кнопку "Показать/Скрыть" пароль')
    def click_show_password(self, password_field):
        eye_button = self.wait_and_click_to_element(password_field)
        #eye_button.wait_and_click_to_element(password_field)





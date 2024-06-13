import allure
from selenium.webdriver.common.by import By
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Заполняем поле Email')
    def set_email_input(self, email):
        element = self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        element.send_keys(email)

    @allure.step('Кликаем на Восстановить пароль')
    def click_password_restore(self):
        return self.click_to_element_with_js(ForgotPasswordPageLocators.RESTORE_BUTTON)

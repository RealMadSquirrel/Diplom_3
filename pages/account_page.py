import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage

class AccountPage(BasePage):

    @allure.step('Кликаем на кнопку «История заказов»')
    def click_button_history(self):
        self.wait_and_click_to_element(AccountPageLocators.HISTORY_ORDER_BUTTON)



    @allure.step('Кликаем по кнопке «Выход»')
    def click_restore_password(self):
        self.wait_and_find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.click_to_element_with_js(LoginPageLocators.FORGOT_PASSWORD)
        return ForgotPasswordPage(self.driver)


    @allure.step('Поиск идентификатора заказа в истории заказов')
    def search_order_id_in_history(self):
       return self.wait_and_find_element(AccountPageLocators.ORDER_IDENTIFICATOR).text
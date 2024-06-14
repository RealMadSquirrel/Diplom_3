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

    @allure.step('Поиск идентификатора заказа в истории заказов')
    def search_order_id_in_history(self):
       return self.wait_and_find_element(AccountPageLocators.ORDER_IDENTIFICATOR_IN_HISTORY).text

    @allure.step('Поиск и клик на Историю заказов')
    def search_and_click_history_button(self):
        return self.wait_and_click_to_element(AccountPageLocators.HISTORY_ORDER_BUTTON)

    @allure.step('Получение атрибута aria-current у Истории заказов')
    def get_atribute_history_button(self):
        return self.wait_and_find_element(AccountPageLocators.HISTORY_ORDER_BUTTON).get_attribute('aria-current')

    @allure.step('Поиск и клик на Выход')
    def search_and_click_exit(self):
        return self.wait_and_click_to_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Поиск заголовка Профиль')
    def search_profile_title(self):
        return self.wait_and_find_element(AccountPageLocators.PROFILE_TITLE).text
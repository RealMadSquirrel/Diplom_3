import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class OrderLentaPage(BasePage):

    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_personal_account(self):
        self.wait_and_click_to_element(MainPageLocators.PERSONAL_BUTTON)

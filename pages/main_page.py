from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from pages.orders_lenta_page import OrderLentaPage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    CURRENT_ACCOUNT_LOGIN = (By.XPATH, "//p[@class = 'header__user']")

    @allure.step('Ожидаем элемент и отдаем текст')
    def check_invisible_cross(self):
        current_user = self.wait_and_find_element(self.CURRENT_ACCOUNT_LOGIN)
        return current_user.text

    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_personal_account(self):
        self.wait_and_find_element(MainPageLocators.PERSONAL_BUTTON)
        self.wait_and_click_to_element(MainPageLocators.PERSONAL_BUTTON)

    @allure.step('Кликаем на кнопку Лента заказов')
    def click_order_lenta(self):
        self.wait_and_find_element(MainPageLocators.LENTA_BUTTON)
        self.click_to_element_with_js(MainPageLocators.LENTA_BUTTON)
        return OrderLentaPage(self.driver)

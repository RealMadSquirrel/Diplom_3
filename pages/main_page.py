from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from pages.orders_lenta_page import OrderLentaPage
from locators.main_page_locators import MainPageLocators
from data import Urls


class MainPage(BasePage):

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

    @allure.step('Ожидание смены страницы main')
    def wait_for_url_changes_main(self):
        self.wait_url_changes(Urls.BASE_URL)

    @allure.step('Добавление ингредиента в заказ и оформление')
    def add_ingredient_to_order_and_checkout(self):
        self.wait_and_find_element(MainPageLocators.INGREDIENT_BUTTON_KRATEN)
        self.add_ingredient_to_order(MainPageLocators.INGREDIENT_BUTTON_KRATEN, MainPageLocators.TARGET)
        self.wait_and_find_element(MainPageLocators.CHECKOUT_BUTTON)
        self.click_to_element_with_js(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Перетаскивание ингредиента')
    def add_ingredient_to_order_main_page(self):
        self.add_ingredient_to_order(MainPageLocators.INGREDIENT_BUTTON_KRATEN, MainPageLocators.TARGET)

    @allure.step('Получение счетчика ингредиента')
    def count_ingredient(self):
        return self.wait_and_find_element(MainPageLocators.COUNT_INGREDIENTS).text

    @allure.step('Поиск фразы Ваш заказ начали готовить')
    def search_checkout_text(self):
        return self.wait_and_find_element(MainPageLocators.CHECKOUT_TEXT).text

    @allure.step('Клик на крестик, закрыть окно с заказом')
    def click_to_cross(self):
        self.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)

    @allure.step('Получение номера заказа в модальном окне')
    def search_number_orders_in_modal_window(self):
        return self.get_new_order_number(MainPageLocators.NUMBER_ORDERS)

    @allure.step('Поиск заголовка Соберите бургер')
    def search_title_collect_burger(self):
        return self.wait_and_find_element(MainPageLocators.BUILD_BURGER).text

    @allure.step('Выбор ингредиента')
    def click_to_ingredient(self):
        self.click_to_element_with_js(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Поиск заголовка Детали ингредиента')
    def search_title_details_ingredient(self):
        return self.wait_and_find_element(MainPageLocators.H2_DETAILS_INGR).text

    @allure.step('Кликаем на ингредиент и закрываем окно нажатием на крестик')
    def click_to_ingredient_and_closed(self):
        self.click_to_element_with_js(MainPageLocators.INGREDIENT_BUTTON)
        self.click_to_element_with_js(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверяем, что окно с информацией по ингредиенту, при нажатии на крестик пропало')
    def info_ingredient_is_invisible(self):
        return self.element_is_invisible(MainPageLocators.CROSS_BUTTON)







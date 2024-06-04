import allure
import time
from pages.main_page import MainPage
from locators.main_functionality_locators import MainFuncPageLocators
from data import Urls
from data import Data
from seletools.actions import drag_and_drop
import selectors


class TestMainFuncPage:

    @allure.title("Клик по кнопке Конструктор")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_with_js(MainFuncPageLocators.CONSTRUCTOR_BUTTON)
        assert main_page.wait_and_find_element(MainFuncPageLocators.BUILD_BURGER).text == 'Соберите бургер'

    @allure.title("Клик по кнопке Лента")
    def test_click_lenta(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_with_js(MainFuncPageLocators.LENTA_BUTTON)
        assert main_page.wait_and_find_element(MainFuncPageLocators.LENTA_ORDERS).text == 'Лента заказов'

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_with_js(MainFuncPageLocators.INGREDIENT_BUTTON)
        assert main_page.wait_and_find_element(MainFuncPageLocators.H2_DETAILS_INGR).text == 'Детали ингредиента'

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_element_with_js(MainFuncPageLocators.INGREDIENT_BUTTON)
        main_page.click_to_element_with_js(MainFuncPageLocators.CROSS_BUTTON)
        assert main_page.wait_find_element_invisible(MainFuncPageLocators.CROSS_BUTTON)









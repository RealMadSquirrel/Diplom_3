import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import allure
import selectors
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем и находим элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем, что элемент будет кликабелен и кликаем')
    def wait_clickable_find_element_click(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Проверяем смену url')
    def url_changes(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    @allure.step('Находим элемент и вводим текст')
    def find_element_and_send_keys(self, locator, key):
        return self.driver.find_element(*locator).send_keys(*key)

    @allure.step('Кликаем на элемент')
    def click(self, locator):
        return self.driver.find_element(*locator).click()

    @allure.step('Кликаем на элемент с ожиданием')
    def wait_and_click_to_element(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Кликаем на элемент с JS')
    def click_to_element_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)


    @allure.step('Ожидаем, что элемент visible')
    def wait_clickable_find_element_click(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].style.visibility='visible';", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидаем, что элемент invisible')
    def element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание элемента')
    def add_ingredient_to_order(self, source, target):
        source = self.driver.find_element(*source)
        target = self.driver.find_element(*target)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ожидаем, что элемент invisible')
    def element_is_presence_of_element_located(self, locator):
        but = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located(locator))
        but.click()

    def click_and_hold(self,locator):
        element = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.double_click(element)

    @allure.step('Получить номер оформленного заказа')
    def get_new_order_number(self, locator):
        WebDriverWait(self.driver, 30).until(lambda driver:self.wait_and_find_element(locator).text != '9999')
        return self.wait_and_find_element(locator).text

    @allure.step('Ожидание, что заказ в работе')
    def get_order_number_in_work(self, locator):
        WebDriverWait(self.driver, 30).until(lambda driver: self.wait_and_find_element(locator).text != 'Все текущие заказы готовы!')
        return self.wait_and_find_element(locator).text


    @allure.step('Дожидаемся, пока поменяется страница')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_changes(url))

    @allure.step('Проверяем какая страница сейчас')
    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))



from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем и находим элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Берем куки')
    def get_cookie(self, url):
        self.driver.get_cookies()

    @allure.step('Находим элемент и вводим текст')
    def find_element_and_send_keys(self, locator, key):
        return self.driver.find_element(*locator).send_keys(*key)

    @allure.step('Кликаем на элемент')
    def click(self, locator):
        return self.driver.find_element(*locator).click()


    def click_and_hold(self, locator):
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(driver).click_and_hold(clickable).perform()

    @allure.step('Кликаем на элемент с ожиданием')
    def wait_and_click_to_element(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Кликаем на элемент с JS')
    def click_to_element_with_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

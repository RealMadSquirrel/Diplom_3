from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    CURRENT_ACCOUNT_LOGIN = (By.XPATH, "//p[@class = 'header__user']")

    def get_current_user(self):
        current_user = self.wait_and_find_element(self.CURRENT_ACCOUNT_LOGIN)
        return current_user.text
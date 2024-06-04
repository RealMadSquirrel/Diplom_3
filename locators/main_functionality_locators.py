import allure
from selenium.webdriver.common.by import By

class MainFuncPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']/parent::a") # кнопка Конструктор
    BUILD_BURGER = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    LENTA_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']/parent::a")
    LENTA_ORDERS = (By.XPATH, "//h1[text() = 'Лента заказов']")
    INGREDIENT_BUTTON = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']/parent::a")
    H2_DETAILS_INGR = (By.XPATH, "//h2[text() = 'Детали ингредиента']")
    CROSS_BUTTON = (By.XPATH, "//button[contains(@*, 'button') and contains(@class, 'Modal_modal__close_modified')]")
    COUNT_INGREDIENTS = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']/following::p")
    TARGET = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
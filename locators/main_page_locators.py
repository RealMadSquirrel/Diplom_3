import allure
from selenium.webdriver.common.by import By

class MainPageLocators:

    PERSONAL_BUTTON = (By.XPATH, "//a[@href = '/account']") # ссылка на Личный Кабинет
    LENTA_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']/parent::a")

    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input[@type = 'text']") #поле для ввода почты
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']") #поле для ввода пароля

    NUMBER_ORDERS = (By.XPATH, "//p[text() = 'идентификатор заказа']/preceding-sibling::h2")
    BUILD_BURGER = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    INGREDIENT_BUTTON = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']/parent::a")
    H2_DETAILS_INGR = (By.XPATH, "//h2[text() = 'Детали ингредиента']")

    CROSS_BUTTON = (By.XPATH, "//button[contains(@*, 'button') and contains(@class, 'Modal_modal__close_modified')]")

    COUNT_INGREDIENTS = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']/following::p[1]")
    TARGET = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
    INGREDIENT_BUTTON_KRATEN = (By.XPATH, "//p[text() = 'Краторная булка N-200i']/parent::a")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    CHECKOUT_TEXT = (By.XPATH, "//p[text() = 'Ваш заказ начали готовить']")




import requests
import random
import string
import allure
from data import Urls


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class UserFactory:
    @staticmethod
    def register_new_user_and_return_load():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "email": login + "@mail.ru",
            "password": password,
            "name": first_name
        }

        return payload


class UserApi:

    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(body):
        return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(user_access_token):
        return requests.delete(Urls.BASE_URL + Urls.DELETE_USER, headers={'Authorization': user_access_token})


class LoginUserApi:
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login(creds):
        return requests.post(Urls.BASE_URL + Urls.LOGIN_API, json=creds)
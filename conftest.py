import pytest
from selenium import webdriver
from data import Urls
import helper
from helper import UserApi
from helper import LoginUserApi


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def create_creds_user():
    creds = helper.UserFactory.register_new_user_and_return_load()
    created_user_request = UserApi.create_user(creds)
    yield creds
    UserApi.delete_user(created_user_request.json()[
                            "accessToken"])

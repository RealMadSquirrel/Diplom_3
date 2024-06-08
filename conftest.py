import pytest
from selenium import webdriver
from data import Urls
import helper


@pytest.fixture(params=['chrome','firefox'])
def driver(request):
    browser = None

    if request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    #browser.get(Urls.BASE_URL)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def create_creds_user():
    creds = helper.UserFactory.register_new_user_and_return_load()
    return creds






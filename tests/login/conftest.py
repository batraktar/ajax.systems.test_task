import pytest

from framework.login_page import LoginPage

# Тут нічого не змінював, так і залишив
@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)

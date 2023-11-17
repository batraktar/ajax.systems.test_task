import pytest
# import logging
from framework.login_page import LoginPage

login_password_data = [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password"),
]

negative_login_password_data = [
    ("1@negative.com", "q"),
    ('2@negative.com', 'w'),
]


@pytest.mark.parametrize(("login", "password"), login_password_data)
def test_user_login_poz(driver, login, password):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.click_login_button()

    assert login_page.is_login_successful(), f"Failed login with {login} and {password}"
    return


@pytest.mark.parametrize(("login", "password"), negative_login_password_data)
def test_user_login_neg(driver, login, password):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.click_login_button()

    assert login_page.is_error_message_displayed(), "Error message should be displayed with " \
                                                    "invalid credentials."

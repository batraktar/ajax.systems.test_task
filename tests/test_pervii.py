import pytest
from appium.webdriver.common.mobileby import MobileBy
# import logging
from framework.login_page import LoginPage
from tests.SideBar.test_sidebar import SideBarTests
from tests.parametrize_file  import login_password_data, negative_login_password_data


@pytest.mark.parametrize(("login", "password"), login_password_data)
def test_user_login_poz(driver, login, password):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.click_login_button()
    side_bar_tests = SideBarTests(driver)
    side_bar_tests.click_menu_drawer()
    side_bar_tests.test_sidebar_elements((MobileBy.ID, "com.ajaxsystems:id/settings"))
    side_bar_tests.test_sidebar_elements((MobileBy.ID, "com.ajaxsystems:id/help"))
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

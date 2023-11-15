from framework.login_page import LoginPage

login = 'qa.ajax.app.automation@gmail.com'
password = 'qa_automation_password'


def test_user_login_poz(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.enter_login(login)
    login_page.enter_password(password)
    login_page.click_login_button()

    assert login_page.is_login_successful(), "Successful login expected, but not achieved."
    return



# Не встиг по часу доробити
# def test_user_login_neg(driver):
#     login_page = LoginPage(driver)
#     login_page.click_login_button()
#     login_page.enter_login(login)
#     login_page.enter_password(password)
#     login_page.click_login_button()

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.page import AppiumPage


class LoginPage(AppiumPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_button_locator = (By.XPATH,
                                     '//android.widget.TextView['
                                     '@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        self.login_input_locator = (By.ID, 'com.ajaxsystems:id/authLoginEmail')
        self.password_input_locator = (By.ID, 'com.ajaxsystems:id/authLoginPassword')

    def click_login_button(self):
        self.click_element(*self.login_button_locator)

    def click_and_clear(self, element):
        element.click()
        element.clear()

    def enter_login(self, username):
        login_input = self.find_element(*self.login_input_locator)
        self.click_and_clear(login_input)

        if login_input:
            ActionChains(self.driver).click(login_input).send_keys(username).perform()
        else:
            raise ValueError("Login input element not found or not interactable.")

    def enter_password(self, password):
        password_input = self.find_element(*self.password_input_locator)
        self.click_and_clear(password_input)

        if password_input:
            ActionChains(self.driver).click(password_input).send_keys(password).perform()
        else:
            raise ValueError("Password input element not found or not interactable")

    def is_login_successful(self):
        # Додайте очікування на появу елемента, який є унікальним для головної сторінки після успішного входу
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'com.ajaxsystems:id/coordinatorLayout'))
            )
            return True
        except TimeoutException:
            return False
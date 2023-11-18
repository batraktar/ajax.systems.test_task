import logging
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


class SideBarTests:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element is not None
        except NoSuchElementException:
            return False

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def click_menu_drawer(self):
        menu_drawer_locator = (MobileBy.ID, "com.ajaxsystems:id/menuDrawer")
        menu_drawer = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(menu_drawer_locator)
        )
        menu_drawer.click()

    def test_sidebar_elements(self, locator):
        self.click_menu_drawer()

        if self.is_element_present(locator):
            logging.info(f"Element with locator {locator} is present.")
        else:
            logging.warning(f"Element with locator {locator} is not present.")

        if self.is_element_visible(locator):
            logging.info(f"Element with locator {locator} is visible.")
        else:
            logging.warning(f"Element with locator {locator} is not visible.")

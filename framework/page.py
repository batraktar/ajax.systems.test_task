# Тут написав за допомогою документації, без використання форумів та інших способів інформації, окрім документації
class AppiumPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_method, value):
        return self.driver.find_element(by_method, value)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

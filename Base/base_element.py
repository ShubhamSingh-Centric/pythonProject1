from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:

    def __init__(self, browser, locator, locator_value):
        self.browser = browser
        self.locator = locator
        self.locator_value = locator_value
        self.element = self.get_element()


    def get_element(self):
        element = WebDriverWait(self.browser, 15)\
            .until(EC.visibility_of_element_located((self.locator, self.locator_value)))
        return element

    def click_element(self):
        self.element.click()

    def get_text(self):
        return self.element.text


# if __name__ == "__main__":
#     e= Element()
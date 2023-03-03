from Base.base_page import BasePage
from Base.base_element import Element
from selenium.webdriver.common.by import By

class GoogleHome(BasePage):

    url = 'https://www.google.com'

    def __init__(self, browser):
        super().__init__(browser, self.url)


    def sign_in_button(self):
        return Element(self.browser, By.XPATH, '//div[@class="gb_Re"]//a[text() = "Sign in"]')

    def my_text(self):
        return Element(self.browser, By.XPATH, '//div[@id="headingSubtext"]//span')

    def email_input_box(self):
        return Element(self.browser, By.XPATH, '//input[@type="email"]')

    def next_button(self):
        return Element(self.browser, By.XPATH, '//span[text()="Next"]')

    def heading_text_after_next(self):
        # return Element(self.browser, By.XPATH, '//h1[@id="headingText"]/span')
        return Element(self.browser, By.XPATH, '//span[text()="Couldn’t sign you in"]')
from Base.base_page import BasePage
from selenium.webdriver.common.by import By


class GooglePage(BasePage):

    url = "https://www.google.com/"

    def input_box(self):
        return self.browser.find_element(By.XPATH, '//input[@name="q"]')

    def tools_button(self):
        return self.browser.find_element(By.ID, 'hdtb-tls')




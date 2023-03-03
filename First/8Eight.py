
from selenium import webdriver
from Base.base_element import Element

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.google.com")

sign_in_button = Element(browser, By.XPATH, '//div[@class="gb_Re"]//a[text() = "Sign in"]')

forget_email_button = Element(browser, By.XPATH, '//button[@jsname="Cuz2Ue"]')


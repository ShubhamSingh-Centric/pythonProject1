from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.google.com")
sign_in_button = browser.find_element(By.XPATH, '//div[@class="gb_Re"]//a[text() = "Sign in"]')

browser.save_screenshot("myscreenshot.png")


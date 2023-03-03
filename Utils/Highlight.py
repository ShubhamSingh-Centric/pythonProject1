from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def highlight(element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)

    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style") != None):
        time.sleep(5)
    apply_style(orignal_style)


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.google.com")
sign_in_button = browser.find_element(By.XPATH, '//div[@class="gb_Re"]//a[text() = "Sign in"]')
highlight(sign_in_button)
# browser.save_screenshot("myscreenshot1.png")

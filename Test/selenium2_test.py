from selenium import webdriver
from First.selenium2 import GooglePage
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

page = GooglePage(browser)
page.go()
page.input_box().send_keys("asdas")
page.input_box().send_keys(Keys.ENTER)
page.tools_button().click()